
The project is WIP.

# How to use

1. Setup and enter pipenv environment
```bash
pipenv sync
pipenv shell
```

2. Run the program
   1. Semantic segmentation (all instances of selected classes are removed)

```bash
python app.py --mode semseg_img

or

python app.py --mode instseg_img
