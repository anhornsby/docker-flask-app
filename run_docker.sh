docker run -it -p 5000:5000 -v $(pwd):/app politics-experiment /bin/bash
# now run the following inside the container 
# webpack --watch &
# python main.py