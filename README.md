# template-ocr-example

### setup
```sh
# install tesseract ocr
sudo apt install tesseract-ocr python3-opencv

# setup python environment
git clone https://github.com/lakshanwd/template-ocr-example.git

# environment setup
cd path/to/repo/template-ocr-example
pipenv install
pipenv install --dev
```

### test
```sh
pipenv run python doc-scanner.py
```