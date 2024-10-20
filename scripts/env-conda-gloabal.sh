
export ENV_NAME="fpga-ui"

# Create a new conda environment
conda create -n $ENV_NAME python=3.12 -y

conda activate $ENV_NAME

python3 -m pip install -r requirements.txt