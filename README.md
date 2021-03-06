# MPM Post-Process

## Features

- [x] Convert HDF5 files to VTP for visualization of different parameters like velocity and strain (note that [mpm code](https://github.com/cb-geo/mpm) outputs stress in VTP format)
- [ ] Analyze different variables such as stress and velocity of certain particles over time

## Dependencies

- Using `python3`
- Using `pip`, `sudo apt-get install python3-pip`
- Matplotlib, `sudo pip3 install matplotlib`, `sudo apt-get install python3-tk`
- Numpy, `sudo pip3 install numpy`
- Pandas, `sudo pip3 install pandas`, `sudo apt-get install python3-tables`
- EVTK `pip3 install evtk` or `sudo apt install mercurial`, `hg clone https://bitbucket.org/pauloh/pyevtk`, `sudo python3 setup.py install`


## Visualization
I personally use [Paraview](https://www.paraview.org/download/). Note that VTK is now deprecated and for material point method 

## References
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_hdf.html)
- [EVTK](https://bitbucket.org/pauloh/pyevtk)
