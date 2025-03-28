import torch
import torch.distributed as dist
import argparse
import os

def init_distributed_mode(master_ip, master_port, local_rank, world_size, backend="gloo"):
    # Get rank and world size from environment variables
    rank = int(local_rank)
    print(rank)
    world_size = int(world_size)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--master_ip", type=str, default="10.10.1.2")
    parser.add_argument("--master_port", type=str, default="12355")
    parser.add_argument("--local_rank", type=int, default=-1, help="For distributed training: local_rank. If single-node training, local_rank defaults to -1.")
    args = parser.parse_args()
    
    master_ip = args.master_ip
    master_port = args.master_port
    local_rank = args.local_rank
    world_size = 4
    
    init_distributed_mode(master_ip, master_port, local_rank, world_size)

