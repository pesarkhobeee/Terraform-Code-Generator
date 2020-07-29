# Terraform-Code-Generator

### Development Environment

At the very beginning, you have to initiate a virtual environment with this:

```
sudo apt-get install -y python3-venv
python3 -m venv venv
```

And then every time that you want to run it:

```
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Running in Production

Please install all the needed dependencies with the help of below command:

```
python -m pip install -r requirements.txt
```

Then you can run the program like this:
 
```
./tcg.py -h
usage: tcg.py [-h] [--output-file-name OUTPUT_FILE_NAME]
              [--log-level LOG_LEVEL]
              Source Destination

Source Destination

positional arguments:
  Source                The configuration file location
  Destination           The output directory for the generated .tf file

optional arguments:
  -h, --help            show this help message and exit
  --output-file-name OUTPUT_FILE_NAME
                        The file name which we will use to save the output
  --log-level LOG_LEVEL
                        Set the logging level. Defaults to WARNING.

```
