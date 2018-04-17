## Images

The images datasets used on paper is listed in text files 'label_{dataset_name}'. 

The files contains informations about each image of dataset, as the following:

  `{dataset_name}/{img_name} {expression_label} {x_right_eye} {y_right_eye} {x_left_eye} {y_left_eye} {person_id} {gender}`
  
  e.g. `RadBoud/Rafd090_27_Caucasian_female_surprised_frontal.jpg 6 277 404 417 406 27 2`


The x and y eyes position is used to spatial normalization images.

File 'MMI_Image_Frames.json' contains information about expression label and frame for each video file in MMI database.
```{
    "100/S001-100.avi": { # video file name
            "0": [        # expression number
                1,        # frames selected
                82
            ], 
            "1": [
                36
            ]
        }
    }
