## Models

You can download the models in this [Google Drive directory](https://drive.google.com/drive/folders/0B28GajqdPp8_eGtfRkxxdWZjY1E).

In this directory, you'll find 10 models (5 for Random and 5 for Tuning). The model name is database name which is testing on:
- CK_Random
- CK_Tuning
- JAFFE_Random
- JAFFE_Tunning
- KDEF_Random
- KDEF_Tuning
- MMI_Random
- MMI_Tuning
- RAFD_Random
- RAFD_Tuning

For each model, you'll find:
- Weights: `{model_name}.caffemodel`
- Mean: `mean.binaryproto`
- Deploy: `deploy.prototxt`


Edit script 'inference.py' setting the 'model_name' to run model using images that can be placed in '/samples' directory.
