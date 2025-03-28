import torch
import torch.distributed as dist
import os

def init_distributed_mode(backend="gloo"):
    # Set up master IP and port
    master_ip = "10.10.1.24"  # The IP of the master node
    master_port = "12355"  # The port to use for communication

    # Get rank and world size from environment variables
    rank = int(os.environ["RANK"])
    print(rank)
    world_size = int(os.environ["WORLD_SIZE"])
    print(world_size)

    # Initialize the process group for distributed training
    dist.init_process_group(
        backend=backend, 
        init_method=f"tcp://{master_ip}:{master_port}",
        world_size=world_size, 
        rank=rank
    )

    # Now you can use distributed data parallelism (DDP), etc.

# This is just for testing purposes, you would need to run this on all nodes
if __name__ == "__main__":
    init_distributed_mode()

