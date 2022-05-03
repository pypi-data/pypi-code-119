#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    : syscall_num.py
@Time    : 2021/11/23 23:45:56
@Author  : Roderick Chan
@Email   : ch22166@163.com
@Desc    : Syscall number of i386 and amd64
'''


__all__ = ["SyscallNumber"]

class SyscallNumber:
    class i386:
        RESTART_SYSCALL = 0
        EXIT = 1
        FORK = 2
        READ = 3
        WRITE = 4
        OPEN = 5
        CLOSE = 6
        WAITPID = 7
        CREAT = 8
        LINK = 9
        UNLINK = 10
        EXECVE = 11
        CHDIR = 12
        TIME = 13
        MKNOD = 14
        CHMOD = 15
        LCHOWN = 16
        BREAK = 17
        OLDSTAT = 18
        LSEEK = 19
        GETPID = 20
        MOUNT = 21
        UMOUNT = 22
        SETUID = 23
        GETUID = 24
        STIME = 25
        PTRACE = 26
        ALARM = 27
        OLDFSTAT = 28
        PAUSE = 29
        UTIME = 30
        STTY = 31
        GTTY = 32
        ACCESS = 33
        NICE = 34
        FTIME = 35
        SYNC = 36
        KILL = 37
        RENAME = 38
        MKDIR = 39
        RMDIR = 40
        DUP = 41
        PIPE = 42
        TIMES = 43
        PROF = 44
        BRK = 45
        SETGID = 46
        GETGID = 47
        SIGNAL = 48
        GETEUID = 49
        GETEGID = 50
        ACCT = 51
        UMOUNT2 = 52
        LOCK = 53
        IOCTL = 54
        FCNTL = 55
        MPX = 56
        SETPGID = 57
        ULIMIT = 58
        OLDOLDUNAME = 59
        UMASK = 60
        CHROOT = 61
        USTAT = 62
        DUP2 = 63
        GETPPID = 64
        GETPGRP = 65
        SETSID = 66
        SIGACTION = 67
        SGETMASK = 68
        SSETMASK = 69
        SETREUID = 70
        SETREGID = 71
        SIGSUSPEND = 72
        SIGPENDING = 73
        SETHOSTNAME = 74
        SETRLIMIT = 75
        GETRLIMIT = 76
        GETRUSAGE = 77
        GETTIMEOFDAY = 78
        SETTIMEOFDAY = 79
        GETGROUPS = 80
        SETGROUPS = 81
        SELECT = 82
        SYMLINK = 83
        OLDLSTAT = 84
        READLINK = 85
        USELIB = 86
        SWAPON = 87
        REBOOT = 88
        READDIR = 89
        MMAP = 90
        MUNMAP = 91
        TRUNCATE = 92
        FTRUNCATE = 93
        FCHMOD = 94
        FCHOWN = 95
        GETPRIORITY = 96
        SETPRIORITY = 97
        PROFIL = 98
        STATFS = 99
        FSTATFS = 100
        IOPERM = 101
        SOCKETCALL = 102
        SYSLOG = 103
        SETITIMER = 104
        GETITIMER = 105
        STAT = 106
        LSTAT = 107
        FSTAT = 108
        OLDUNAME = 109
        IOPL = 110
        VHANGUP = 111
        IDLE = 112
        VM86OLD = 113
        WAIT4 = 114
        SWAPOFF = 115
        SYSINFO = 116
        IPC = 117
        FSYNC = 118
        SIGRETURN = 119
        CLONE = 120
        SETDOMAINNAME = 121
        UNAME = 122
        MODIFY_LDT = 123
        ADJTIMEX = 124
        MPROTECT = 125
        SIGPROCMASK = 126
        CREATE_MODULE = 127
        INIT_MODULE = 128
        DELETE_MODULE = 129
        GET_KERNEL_SYMS = 130
        QUOTACTL = 131
        GETPGID = 132
        FCHDIR = 133
        BDFLUSH = 134
        SYSFS = 135
        PERSONALITY = 136
        AFS_SYSCALL = 137
        SETFSUID = 138
        SETFSGID = 139
        _LLSEEK = 140
        GETDENTS = 141
        _NEWSELECT = 142
        FLOCK = 143
        MSYNC = 144
        READV = 145
        WRITEV = 146
        GETSID = 147
        FDATASYNC = 148
        _SYSCTL = 149
        MLOCK = 150
        MUNLOCK = 151
        MLOCKALL = 152
        MUNLOCKALL = 153
        SCHED_SETPARAM = 154
        SCHED_GETPARAM = 155
        SCHED_SETSCHEDULER = 156
        SCHED_GETSCHEDULER = 157
        SCHED_YIELD = 158
        SCHED_GET_PRIORITY_MAX = 159
        SCHED_GET_PRIORITY_MIN = 160
        SCHED_RR_GET_INTERVAL = 161
        NANOSLEEP = 162
        MREMAP = 163
        SETRESUID = 164
        GETRESUID = 165
        VM86 = 166
        QUERY_MODULE = 167
        POLL = 168
        NFSSERVCTL = 169
        SETRESGID = 170
        GETRESGID = 171
        PRCTL = 172
        RT_SIGRETURN = 173
        RT_SIGACTION = 174
        RT_SIGPROCMASK = 175
        RT_SIGPENDING = 176
        RT_SIGTIMEDWAIT = 177
        RT_SIGQUEUEINFO = 178
        RT_SIGSUSPEND = 179
        PREAD64 = 180
        PWRITE64 = 181
        CHOWN = 182
        GETCWD = 183
        CAPGET = 184
        CAPSET = 185
        SIGALTSTACK = 186
        SENDFILE = 187
        GETPMSG = 188
        PUTPMSG = 189
        VFORK = 190
        UGETRLIMIT = 191
        MMAP2 = 192
        TRUNCATE64 = 193
        FTRUNCATE64 = 194
        STAT64 = 195
        LSTAT64 = 196
        FSTAT64 = 197
        LCHOWN32 = 198
        GETUID32 = 199
        GETGID32 = 200
        GETEUID32 = 201
        GETEGID32 = 202
        SETREUID32 = 203
        SETREGID32 = 204
        GETGROUPS32 = 205
        SETGROUPS32 = 206
        FCHOWN32 = 207
        SETRESUID32 = 208
        GETRESUID32 = 209
        SETRESGID32 = 210
        GETRESGID32 = 211
        CHOWN32 = 212
        SETUID32 = 213
        SETGID32 = 214
        SETFSUID32 = 215
        SETFSGID32 = 216
        PIVOT_ROOT = 217
        MINCORE = 218
        MADVISE = 219
        GETDENTS64 = 220
        FCNTL64 = 221
        GETTID = 224
        READAHEAD = 225
        SETXATTR = 226
        LSETXATTR = 227
        FSETXATTR = 228
        GETXATTR = 229
        LGETXATTR = 230
        FGETXATTR = 231
        LISTXATTR = 232
        LLISTXATTR = 233
        FLISTXATTR = 234
        REMOVEXATTR = 235
        LREMOVEXATTR = 236
        FREMOVEXATTR = 237
        TKILL = 238
        SENDFILE64 = 239
        FUTEX = 240
        SCHED_SETAFFINITY = 241
        SCHED_GETAFFINITY = 242
        SET_THREAD_AREA = 243
        GET_THREAD_AREA = 244
        IO_SETUP = 245
        IO_DESTROY = 246
        IO_GETEVENTS = 247
        IO_SUBMIT = 248
        IO_CANCEL = 249
        FADVISE64 = 250
        EXIT_GROUP = 252
        LOOKUP_DCOOKIE = 253
        EPOLL_CREATE = 254
        EPOLL_CTL = 255
        EPOLL_WAIT = 256
        REMAP_FILE_PAGES = 257
        SET_TID_ADDRESS = 258
        TIMER_CREATE = 259
        TIMER_SETTIME = 260
        TIMER_GETTIME = 261
        TIMER_GETOVERRUN = 262
        TIMER_DELETE = 263
        CLOCK_SETTIME = 264
        CLOCK_GETTIME = 265
        CLOCK_GETRES = 266
        CLOCK_NANOSLEEP = 267
        STATFS64 = 268
        FSTATFS64 = 269
        TGKILL = 270
        UTIMES = 271
        FADVISE64_64 = 272
        VSERVER = 273
        MBIND = 274
        GET_MEMPOLICY = 275
        SET_MEMPOLICY = 276
        MQ_OPEN = 277
        MQ_UNLINK = 278
        MQ_TIMEDSEND = 279
        MQ_TIMEDRECEIVE = 280
        MQ_NOTIFY = 281
        MQ_GETSETATTR = 282
        KEXEC_LOAD = 283
        WAITID = 284
        ADD_KEY = 286
        REQUEST_KEY = 287
        KEYCTL = 288
        IOPRIO_SET = 289
        IOPRIO_GET = 290
        INOTIFY_INIT = 291
        INOTIFY_ADD_WATCH = 292
        INOTIFY_RM_WATCH = 293
        MIGRATE_PAGES = 294
        OPENAT = 295
        MKDIRAT = 296
        MKNODAT = 297
        FCHOWNAT = 298
        FUTIMESAT = 299
        FSTATAT64 = 300
        UNLINKAT = 301
        RENAMEAT = 302
        LINKAT = 303
        SYMLINKAT = 304
        READLINKAT = 305
        FCHMODAT = 306
        FACCESSAT = 307
        PSELECT6 = 308
        PPOLL = 309
        UNSHARE = 310
        SET_ROBUST_LIST = 311
        GET_ROBUST_LIST = 312
        SPLICE = 313
        SYNC_FILE_RANGE = 314
        TEE = 315
        VMSPLICE = 316
        MOVE_PAGES = 317
        GETCPU = 318
        EPOLL_PWAIT = 319
        UTIMENSAT = 320
        SIGNALFD = 321
        TIMERFD_CREATE = 322
        EVENTFD = 323
        FALLOCATE = 324
        TIMERFD_SETTIME = 325
        TIMERFD_GETTIME = 326
        SIGNALFD4 = 327
        EVENTFD2 = 328
        EPOLL_CREATE1 = 329
        DUP3 = 330
        PIPE2 = 331
        INOTIFY_INIT1 = 332
        PREADV = 333
        PWRITEV = 334
        RT_TGSIGQUEUEINFO = 335
        PERF_EVENT_OPEN = 336
        RECVMMSG = 337
        FANOTIFY_INIT = 338
        FANOTIFY_MARK = 339
        PRLIMIT64 = 340
        NAME_TO_HANDLE_AT = 341
        OPEN_BY_HANDLE_AT = 342
        CLOCK_ADJTIME = 343
        SYNCFS = 344
        SENDMMSG = 345
        SETNS = 346
        PROCESS_VM_READV = 347
        PROCESS_VM_WRITEV = 348
        KCMP = 349
        FINIT_MODULE = 350
        SCHED_SETATTR = 351
        SCHED_GETATTR = 352
        RENAMEAT2 = 353
        SECCOMP = 354
        GETRANDOM = 355
        MEMFD_CREATE = 356
        BPF = 357
        EXECVEAT = 358
        SOCKET = 359
        SOCKETPAIR = 360
        BIND = 361
        CONNECT = 362
        LISTEN = 363
        ACCEPT4 = 364
        GETSOCKOPT = 365
        SETSOCKOPT = 366
        GETSOCKNAME = 367
        GETPEERNAME = 368
        SENDTO = 369
        SENDMSG = 370
        RECVFROM = 371
        RECVMSG = 372
        SHUTDOWN = 373
        USERFAULTFD = 374
        MEMBARRIER = 375
        MLOCK2 = 376
        COPY_FILE_RANGE = 377
        PREADV2 = 378
        PWRITEV2 = 379

    class amd64:
        READ = 0
        WRITE = 1
        OPEN = 2
        CLOSE = 3
        STAT = 4
        FSTAT = 5
        LSTAT = 6
        POLL = 7
        LSEEK = 8
        MMAP = 9
        MPROTECT = 10
        MUNMAP = 11
        BRK = 12
        RT_SIGACTION = 13
        RT_SIGPROCMASK = 14
        RT_SIGRETURN = 15
        IOCTL = 16
        PREAD64 = 17
        PWRITE64 = 18
        READV = 19
        WRITEV = 20
        ACCESS = 21
        PIPE = 22
        SELECT = 23
        SCHED_YIELD = 24
        MREMAP = 25
        MSYNC = 26
        MINCORE = 27
        MADVISE = 28
        SHMGET = 29
        SHMAT = 30
        SHMCTL = 31
        DUP = 32
        DUP2 = 33
        PAUSE = 34
        NANOSLEEP = 35
        GETITIMER = 36
        ALARM = 37
        SETITIMER = 38
        GETPID = 39
        SENDFILE = 40
        SOCKET = 41
        CONNECT = 42
        ACCEPT = 43
        SENDTO = 44
        RECVFROM = 45
        SENDMSG = 46
        RECVMSG = 47
        SHUTDOWN = 48
        BIND = 49
        LISTEN = 50
        GETSOCKNAME = 51
        GETPEERNAME = 52
        SOCKETPAIR = 53
        SETSOCKOPT = 54
        GETSOCKOPT = 55
        CLONE = 56
        FORK = 57
        VFORK = 58
        EXECVE = 59
        EXIT = 60
        WAIT4 = 61
        KILL = 62
        UNAME = 63
        SEMGET = 64
        SEMOP = 65
        SEMCTL = 66
        SHMDT = 67
        MSGGET = 68
        MSGSND = 69
        MSGRCV = 70
        MSGCTL = 71
        FCNTL = 72
        FLOCK = 73
        FSYNC = 74
        FDATASYNC = 75
        TRUNCATE = 76
        FTRUNCATE = 77
        GETDENTS = 78
        GETCWD = 79
        CHDIR = 80
        FCHDIR = 81
        RENAME = 82
        MKDIR = 83
        RMDIR = 84
        CREAT = 85
        LINK = 86
        UNLINK = 87
        SYMLINK = 88
        READLINK = 89
        CHMOD = 90
        FCHMOD = 91
        CHOWN = 92
        FCHOWN = 93
        LCHOWN = 94
        UMASK = 95
        GETTIMEOFDAY = 96
        GETRLIMIT = 97
        GETRUSAGE = 98
        SYSINFO = 99
        TIMES = 100
        PTRACE = 101
        GETUID = 102
        SYSLOG = 103
        GETGID = 104
        SETUID = 105
        SETGID = 106
        GETEUID = 107
        GETEGID = 108
        SETPGID = 109
        GETPPID = 110
        GETPGRP = 111
        SETSID = 112
        SETREUID = 113
        SETREGID = 114
        GETGROUPS = 115
        SETGROUPS = 116
        SETRESUID = 117
        GETRESUID = 118
        SETRESGID = 119
        GETRESGID = 120
        GETPGID = 121
        SETFSUID = 122
        SETFSGID = 123
        GETSID = 124
        CAPGET = 125
        CAPSET = 126
        RT_SIGPENDING = 127
        RT_SIGTIMEDWAIT = 128
        RT_SIGQUEUEINFO = 129
        RT_SIGSUSPEND = 130
        SIGALTSTACK = 131
        UTIME = 132
        MKNOD = 133
        USELIB = 134
        PERSONALITY = 135
        USTAT = 136
        STATFS = 137
        FSTATFS = 138
        SYSFS = 139
        GETPRIORITY = 140
        SETPRIORITY = 141
        SCHED_SETPARAM = 142
        SCHED_GETPARAM = 143
        SCHED_SETSCHEDULER = 144
        SCHED_GETSCHEDULER = 145
        SCHED_GET_PRIORITY_MAX = 146
        SCHED_GET_PRIORITY_MIN = 147
        SCHED_RR_GET_INTERVAL = 148
        MLOCK = 149
        MUNLOCK = 150
        MLOCKALL = 151
        MUNLOCKALL = 152
        VHANGUP = 153
        MODIFY_LDT = 154
        PIVOT_ROOT = 155
        _SYSCTL = 156
        PRCTL = 157
        ARCH_PRCTL = 158
        ADJTIMEX = 159
        SETRLIMIT = 160
        CHROOT = 161
        SYNC = 162
        ACCT = 163
        SETTIMEOFDAY = 164
        MOUNT = 165
        UMOUNT2 = 166
        SWAPON = 167
        SWAPOFF = 168
        REBOOT = 169
        SETHOSTNAME = 170
        SETDOMAINNAME = 171
        IOPL = 172
        IOPERM = 173
        CREATE_MODULE = 174
        INIT_MODULE = 175
        DELETE_MODULE = 176
        GET_KERNEL_SYMS = 177
        QUERY_MODULE = 178
        QUOTACTL = 179
        NFSSERVCTL = 180
        GETPMSG = 181
        PUTPMSG = 182
        AFS_SYSCALL = 183
        TUXCALL = 184
        SECURITY = 185
        GETTID = 186
        READAHEAD = 187
        SETXATTR = 188
        LSETXATTR = 189
        FSETXATTR = 190
        GETXATTR = 191
        LGETXATTR = 192
        FGETXATTR = 193
        LISTXATTR = 194
        LLISTXATTR = 195
        FLISTXATTR = 196
        REMOVEXATTR = 197
        LREMOVEXATTR = 198
        FREMOVEXATTR = 199
        TKILL = 200
        TIME = 201
        FUTEX = 202
        SCHED_SETAFFINITY = 203
        SCHED_GETAFFINITY = 204
        SET_THREAD_AREA = 205
        IO_SETUP = 206
        IO_DESTROY = 207
        IO_GETEVENTS = 208
        IO_SUBMIT = 209
        IO_CANCEL = 210
        GET_THREAD_AREA = 211
        LOOKUP_DCOOKIE = 212
        EPOLL_CREATE = 213
        EPOLL_CTL_OLD = 214
        EPOLL_WAIT_OLD = 215
        REMAP_FILE_PAGES = 216
        GETDENTS64 = 217
        SET_TID_ADDRESS = 218
        RESTART_SYSCALL = 219
        SEMTIMEDOP = 220
        FADVISE64 = 221
        TIMER_CREATE = 222
        TIMER_SETTIME = 223
        TIMER_GETTIME = 224
        TIMER_GETOVERRUN = 225
        TIMER_DELETE = 226
        CLOCK_SETTIME = 227
        CLOCK_GETTIME = 228
        CLOCK_GETRES = 229
        CLOCK_NANOSLEEP = 230
        EXIT_GROUP = 231
        EPOLL_WAIT = 232
        EPOLL_CTL = 233
        TGKILL = 234
        UTIMES = 235
        VSERVER = 236
        MBIND = 237
        SET_MEMPOLICY = 238
        GET_MEMPOLICY = 239
        MQ_OPEN = 240
        MQ_UNLINK = 241
        MQ_TIMEDSEND = 242
        MQ_TIMEDRECEIVE = 243
        MQ_NOTIFY = 244
        MQ_GETSETATTR = 245
        KEXEC_LOAD = 246
        WAITID = 247
        ADD_KEY = 248
        REQUEST_KEY = 249
        KEYCTL = 250
        IOPRIO_SET = 251
        IOPRIO_GET = 252
        INOTIFY_INIT = 253
        INOTIFY_ADD_WATCH = 254
        INOTIFY_RM_WATCH = 255
        MIGRATE_PAGES = 256
        OPENAT = 257
        MKDIRAT = 258
        MKNODAT = 259
        FCHOWNAT = 260
        FUTIMESAT = 261
        NEWFSTATAT = 262
        UNLINKAT = 263
        RENAMEAT = 264
        LINKAT = 265
        SYMLINKAT = 266
        READLINKAT = 267
        FCHMODAT = 268
        FACCESSAT = 269
        PSELECT6 = 270
        PPOLL = 271
        UNSHARE = 272
        SET_ROBUST_LIST = 273
        GET_ROBUST_LIST = 274
        SPLICE = 275
        TEE = 276
        SYNC_FILE_RANGE = 277
        VMSPLICE = 278
        MOVE_PAGES = 279
        UTIMENSAT = 280
        EPOLL_PWAIT = 281
        SIGNALFD = 282
        TIMERFD_CREATE = 283
        EVENTFD = 284
        FALLOCATE = 285
        TIMERFD_SETTIME = 286
        TIMERFD_GETTIME = 287
        ACCEPT4 = 288
        SIGNALFD4 = 289
        EVENTFD2 = 290
        EPOLL_CREATE1 = 291
        DUP3 = 292
        PIPE2 = 293
        INOTIFY_INIT1 = 294
        PREADV = 295
        PWRITEV = 296
        RT_TGSIGQUEUEINFO = 297
        PERF_EVENT_OPEN = 298
        RECVMMSG = 299
        FANOTIFY_INIT = 300
        FANOTIFY_MARK = 301
        PRLIMIT64 = 302
        NAME_TO_HANDLE_AT = 303
        OPEN_BY_HANDLE_AT = 304
        CLOCK_ADJTIME = 305
        SYNCFS = 306
        SENDMMSG = 307
        SETNS = 308
        GETCPU = 309
        PROCESS_VM_READV = 310
        PROCESS_VM_WRITEV = 311
        KCMP = 312
        FINIT_MODULE = 313
        SCHED_SETATTR = 314
        SCHED_GETATTR = 315
        RENAMEAT2 = 316
        SECCOMP = 317
        GETRANDOM = 318
        MEMFD_CREATE = 319
        KEXEC_FILE_LOAD = 320
        BPF = 321
        EXECVEAT = 322
        USERFAULTFD = 323
        MEMBARRIER = 324
        MLOCK2 = 325
        COPY_FILE_RANGE = 326
        PREADV2 = 327
        PWRITEV2 = 328