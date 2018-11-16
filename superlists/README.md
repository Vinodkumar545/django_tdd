## Complete process steps of the project in brief

1. Inputs are either PDFs or Images which are uploaded by **end user**

2. If files uploaded are PDFs, those are converted to images using **imagemagic/wand** library

3. These Images to undergo **pre-processing technique** 

4. This technique removes noise, skew, rotation, super resolution on the images

4. Once pre-processing technique is complete, multiple page single file image are converted into one single image

5. Imagess now undergoes OCR mechanism performed either by **tessaract** or **ocrmypdf** OCR Engine

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

6. PDFs are OCRized and are now used to extract the data points information as per the business requirement

6. Once data points are extracted, those are shown on the UI & user can verify/edit/delete datapoint accordingly
