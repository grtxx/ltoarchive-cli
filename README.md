### LTO Archive System

#### System Structure
The user interface of the system is located within the archive and storage modules in PTs. However, the interface only sends API calls to the LTO archive server. The archive server runs on the LTO Manager machine and is responsible for keeping the file systems of the archives up-to-date and handling requests. The archive server can be accessed via an HTTP API, which both the CLI and web interface can connect to.

#### LTO Cartridge Folder Structure
The system operates with LTFS cartridges and IBM Spectrum Archive LE. It supports multiple separate archives, known as archive domains. On the tapes, the top directory level is always the domain, and the directory structure beneath it corresponds to the folder structure of that domain:

```
CARTRIDGE_ROOT
└── DOMAIN1
    ├── Folder
    │   └── Subfolder
    └── ...
└── DOMAIN2
    └── Folder
    └── ...
```

#### CLI
The CLI interface of the archive system is accessible via the `arcli` program on the LTO Manager machine. In addition to the CLI program, the IBM Spectrum Archive CLI is also a useful tool for managing the library.

Usage:
```
arcli <topic> <command> [<parameters>]
```

#### Available Options

| Short Version | Long Version | Description |
|---------------|--------------|-------------|
| -s            | --server     | The hostname of the LTO archive server - defaults to localhost, so it's not necessary to specify |
| -p            | --port       | The port of the LTO archive server - defaults to 8000, so it's not necessary to specify |
| -n            | --copynumber | Option to specify copyNumber - see: tape add |
| -d            | --domain     | Option to specify domain - see: project check |

#### Available Commands

##### domain
- **list**: `arcli domain list`  
  Returns a JSON list of existing domains in the archive system.
  
- **create**: `arcli domain create <DOMAIN>`  
  Creates a new archive domain.
  
- **drop**: `arcli domain drop <DOMAIN>`  
  Deletes an existing archive domain.

##### job
- **list**: `arcli job list`  
  Returns data for the last 100 requests. This is called by the PT when displaying restore tasks.
  
- **pause**: `arcli job pause <jobId>`  
  Stops the task with the specified ID. This applies only to tasks with the status TAPE-OPERATIONS or RESTORING. The job status changes to PAUSED, but ongoing copying will finish.
  
- **continue**: `arcli job continue <jobId>`  
  Continues serving jobs with PAUSED or FREESPACE-STOP status. This does not bypass empty space restrictions. Upon continuation, the system might not prioritize the task: if serving from another cartridge and no free drive is available, it will complete the current task before resuming the paused one.

##### tape
- **list**: `arcli tape list`  
  Lists the LTO cartridges registered in the archive. Not all registered cartridges need to be available in the library. Each tape has a "copyNumber" attribute. The system will fulfill requests from the available tape with the smallest copyNumber.
  
- **add**: `arcli tape add -n 0 <TAPE_LABEL>`  
  Registers a new tape in the archive. The -n parameter specifies the copyNumber of the new tape. If a tape that already exists is created, the program updates the tape with the provided data - e.g., changing the copyNumber.
  
- **updatecontent**: `arcli tape updatecontent <TAPE_LABEL>`  
  Updates the archive with the contents of the specified tape. If the tape is known, the program schedules the cartridge for processing. The process status can be checked with the `arcli system tasks` command.
  
- **clone**: `arcli tape clone <SRC_TAPE> <DST_TAPE>`  
  Clones the content of SRC_TAPE to DST_TAPE in the virtual file systems of the archive. Useful if file dates or other parameters differ between the tapes but the content is known to be identical. NOTE: File positions may not be identical, so restoring from a cloned tape could be problematic if files were not written in the same order on both tapes.
  
- **drop**: `arcli tape drop <TAPE_LABEL>`  
  Deletes the specified tape from the archive. The tape's content disappears from the virtual file systems, and the tape is unregistered from the system.
  
- **workercount**
  - **get**: `arcli tape workercount get`  
    Returns the number of drives the LTO archive is currently using.
    
  - **set**: `arcli tape workercount set <COUNT>`  
    Sets the number of drives the LTO archive can use. Important when other tasks need access to the library. This command ensures that the archive leaves drives available for other tasks (e.g., writing).

##### project
- **check**: `arcli project check -d <DOMAIN> <FOLDER>`  
  Returns whether the specified folder is within the given domain.

##### system
- **destinations**: `arcli system destinations`  
  Returns the available request destinations.
  
- **tasks**: `arcli system tasks`  
  Returns the currently running and waiting processes.
  