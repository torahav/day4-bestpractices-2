import numpy
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()
#sumRank = numpy.zeros(1)

if rank == 1:
    print "Process", rank comm.Send(rank, dest=0)
if rank == 0:
    #sumRank[0] = rank + comm.Recv(rank, source=1)
    sum += comm.recv(rank, source=1)
    print "Sum of ranks", sumRank[0]
    
# Haven't solved this yet