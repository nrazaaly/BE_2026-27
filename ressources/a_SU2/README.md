# Installing SU2 8.5.0 on Linux (Ubuntu)

This tutorial explains how to install **SU2 8.5.0 (Harrier)** from source on Ubuntu Linux.

## 1. Install dependencies and paraview

Open a terminal and run:

```bash
sudo apt update
sudo apt install -y build-essential python3 python3-dev openmpi-bin libopenmpi-dev
sudo apt install -y paraview
```

## 2. Download SU2 8.5.0

Download the source code directly from GitHub:

**[Download SU2 8.5.0 (ZIP)](https://github.com/su2code/SU2/archive/refs/tags/v8.5.0.zip)**

Extract the ZIP archive:

```bash
cd ~/Téléchargements
unzip v8.5.0.zip
```

Check where you are: 
```bash
pwd 
```

List of files/folders in current folder: 
```bash
ls
```

Move the folder to Documents, erase zip file, and go to the SU2 folder:
```bash
mv SU2-8.5.0  ~/Documents
rm -r v8.5.9.zip
cd ~/Documents
```


Enter the extracted directory:

```bash
cd SU2-8.5.0
```

## 3. Compile SU2

Configure the compilation with MPI support:

```bash
./meson.py setup build --prefix="$HOME/SU2-8.5.0-install" -Dwith-mpi=enabled
```

Compile using 4 CPU cores, then install:

```bash
./ninja -C build -j 4
./ninja -C build install
```


## 4. Configure the environment

Add the following lines to your `~/.bashrc` file and reload configuration:

```bash
echo 'export SU2_HOME="$HOME/Documents/SU2-8.5.0"' >> ~/.bashrc
echo 'export SU2_RUN="$HOME/SU2-8.5.0-install/bin"' >> ~/.bashrc
echo 'export PATH="$SU2_RUN:$PATH"' >> ~/.bashrc
echo 'export PYTHONPATH="$SU2_RUN:$PYTHONPATH"' >> ~/.bashrc
source ~/.bashrc
```


## 5. Test the installation

Run:

```bash
SU2_CFD -h
```

If the help message appears, SU2 is correctly installed!

## 6. Run a simulation

Go to the directory containing your configuration file (`.cfg`):

```bash
cd path/to/your/simulation
```

Run a serial simulation:

```bash
SU2_CFD config.cfg
```

Or run a parallel simulation using 4 MPI processes:

```bash
mpirun -np 4 SU2_CFD config.cfg
```

---

### Useful links

* [Official SU2 website](https://su2code.github.io/)
* [SU2 GitHub repository](https://github.com/su2code/SU2)
* [SU2 documentation](https://su2code.github.io/docs/)
