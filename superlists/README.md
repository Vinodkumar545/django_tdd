

## Complete process steps of the project in brief

1. Inputs are either PDFs or Images which are uploaded by **end user**

2. If files uploaded are PDFs, those are converted to images using **imagemagic/wand** library

3. These Images to undergo **pre-processing technique** 

4. This technique removes noise, skew, rotation, super resolution on the images

4. Once pre-processing technique is complete, multiple page single file image are converted into one single image

5. Images now undergoes OCR mechanism performed either by **tessaract** or **ocrmypdf** OCR Engine

    * For terrasact OCR Engine: Inputs are images, but the output can be text/pdf files

        | Input | Output |
        | :---: | :---:  |
        | .tif or .png | .txt |
        | .tif or .png | .pdf |

    * For ocrmypdf OCR Engine: Inputs are PDFs, but the output can be text/pdf files

        | Input | Output |
        | :---: | :---:  |
        | .pdf | .txt |
        | .pdf | .pdf |

5. OCR mechanism returns the output in **PDF** for further processing

6. PDFs are now OCRized and are used to extract the data points information as per the business requirement

6. Once data points are extracted, those are shown on the UI & user can verify/edit/delete datapoint accordingly

## Installation

```
pip install -r requirements.txt
```
### Installating ocrmypdf and tesseract-ocr in ubuntu 16.04

> No package is currently available for Ubuntu 16.04, but you can install the dependencies manually:

```
sudo apt-get update
sudo apt-get install \
    ghostscript \
    libexempi3 \
    pngquant \
    python3-cffi \
    python3-pip \
    qpdf \
    tesseract-ocr \
    unpaper
```

> If you wish install OCRmyPDF for the current user, and ensure that the PATH environment variable contains $HOME/.local/bin.

```
export PATH=$HOME/.local/bin:$PATH
pip3 install --user ocrmypdf
```

> Alternately, you can install ocrmypdf system-wide. (Not recommended.)

```
sudo pip3 install ocrmypdf
```
> At your option, you may upgrade Ubuntu 16.04 LTS to Tesseract 4.0 for improved OCR results.

```
sudo apt-get install -y software-properties-common python-software-properties
sudo add-apt-repository ppa:alex-p/tesseract-ocr -y
sudo apt-get update
sudo apt-get upgrade tesseract-ocr
```
### Terraract command to perform OCR on the images

## Command to convert image to TEXT using tessarct

> tesseract input_file output_file --psm 1 oem 1 txt

```
tesseract ../images/sample.tif ../images/output/sample --psm 1 oem 1

(or)

tesseract ../images/sample.tif ../images/output/sample --psm 1 oem 1 txt
```

## Command to convert image to PDF using tessarct

> tessaract input_file output_file --psm 1 oem 1 pdf

```
tessarct ../images/sample.tif ../images/output/sample --psm 1 oem 1 pdf
```
**Note:** _for the output_file, please don't provide file extension, as command would automatically do it._

### ocrmypdf command to perform OCR on the pdfs

## Command to OCR PDF to TEXT using ocrmypdf

> ocrmypdf --force-ocr --pdf-renderer hocr --output-type txt --max-image-mpixels 0 input_file output_file

```
ocrmypdf --force-ocr --pdf-renderer hocr --output-type txt --max-image-mpixels 0 ../pdfs/sample.pdf ../pdfs/output/sample.txt
```

## Command to OCR PDF to PDF using ocrmypdf

> ocrmypdf --force-ocr --pdf-renderer hocr --output-type pdf --max-image-mpixles 0 input_file output_file

```
ocrmypdf --force-ocr --pdf-renderer hocr --output-type pdf --max-image-mpixles 0 ../pdfs/sample.pdf ../pdfs/output/sample.pdf
```

