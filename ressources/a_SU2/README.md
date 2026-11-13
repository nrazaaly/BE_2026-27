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



## 5. Test the installation on a NACA 0012 airfoil

Download the two files from the GitHub a_testCases/naca/ directory:

- `naca.cfg` – SU2 configuration file
- `mesh.su2` – computational mesh

Open a terminal and create a directory for the test:

```bash
mkdir -p ~/Documents/test/naca
```

Copy the downloaded files into the test directory:

```bash
cp ~/Downloads/naca.cfg ~/Documents/test/naca/
cp ~/Downloads/mesh.su2 ~/Documents/test/naca/
```

Go to the test directory:

```bash
cd ~/Documents/test/naca
```

Run the simulation:

```bash
SU2_CFD naca.cfg
```

Once the simulation has converged, open the solution in ParaView:

```bash
paraview flow.vtu
```

