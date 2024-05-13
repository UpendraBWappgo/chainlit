echo [$(date)]: "START"
echo [$(date)]: "creating a conda env with python 3.9"
conda create --prefix ./env python=3.9 -y
echo [$(date)]: "created conda env"
echo [$(date)]: "activated conda env"
echo [$(date)]: "installing requirements"
pip install -r requirements.txt 
echo [$(date)]: "installed all"
echo [$(date)]: "END"