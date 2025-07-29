# import  tkinter library
from tkinter import *
# access messagebox and ttk's function (ttk -> combobox)
from tkinter import ttk,messagebox
# access filedialogue box 
from tkinter import filedialog
# import pillow library for images
from PIL import  ImageTk, Image
from datetime import date
import sys
import os
# import pyglet
import threading


# global variables
input_dir = None
input_image_for_evaluation = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


def dashboard_fn(loginscreen_image,mainframe,Width,Height):

    #design_1
    design_1 = Label(mainframe,bd=2,bg='black')
    design_1.place(x=Width*0.025,y=Height*0.135,width=Width*0.93,height=Height*0.003)

    #design_2
    design_2 = Label(mainframe,bd=2,bg='black')
    design_2.place(x=Width*0.025,y=Height*0.2,width=Width*0.93,height=Height*0.003)

    # --------------------------------------------------------------------------------------------------
    # row 1
    # --------------------------------------------------------------------------------------------------

    # logo image (use PIL library) -> access image from the system
    logo_image = Image.open(resource_path("Images\\logo.png"))
    # resize the image and apply a high-quality down sampling filter
    logo_image = logo_image.resize((int(Height*0.23),int(Height*0.1)), Image.Resampling.LANCZOS)
    # PhotoImage class is used to add image to widgets, icons etc
    logo_image = ImageTk.PhotoImage(logo_image)

    #logo_label
    logo_label = Label(mainframe,bd=0,bg='#f0f0f0',image=logo_image)
    logo_label.image = logo_image
    logo_label.place(x=Width*0.025,y=Height*0.02,width=Width*0.12,height=Height*0.1)

    # upload_dataset_label
    font_  = ('Lexend','9','bold')
    upload_dataset_label = Button(mainframe,text='Upload Dataset :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w', cursor='hand2')
    upload_dataset_label.place(x=Width*0.025,y=Height*0.154,width=Width*0.08,height=Height*0.03)

    # path_label
    font_  = ('Lexend','9','bold')
    path_label = Button(mainframe,text='Dataset Path :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w', cursor='hand2')
    path_label.place(x=Width*0.188,y=Height*0.154,width=Width*0.07,height=Height*0.03)

    #path_entry
    path_entry = Entry(mainframe,justify=LEFT,bd=1,fg='black',bg='#f0f0f0',font=('Lexend','9'), state='readonly')
    path_entry.place(x=Width*0.27,y=Height*0.148,width=Width*0.31,height=Height*0.04)
    path_entry.insert(0,'    ')
    
    # dataset_status_label
    font_  = ('Lexend','9','bold')
    dataset_status_label = Button(mainframe,text='Dataset Status :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w', cursor='hand2')
    dataset_status_label.place(x=Width*0.59,y=Height*0.154,width=Width*0.1,height=Height*0.03)

    #dataset_status_entry
    dataset_status_entry = Entry(mainframe,justify=LEFT,bd=1,fg='black',bg='#f0f0f0',font=('Lexend','9'), state='readonly')
    dataset_status_entry.place(x=Width*0.675,y=Height*0.148,width=Width*0.28,height=Height*0.04)
    dataset_status_entry.insert(0,'   ')

    # --------------------------------------------------------------------------------------------------
    # row 2
    # --------------------------------------------------------------------------------------------------

    # frame 1
    # model_training_frame
    font_  = ('Lexend','9','bold')
    model_training_frame = LabelFrame(mainframe,bg='#f0f0f0',bd=2,font=font_,text='  Model Training  ')
    model_training_frame.place(x=Width*0.025,y=Height*0.21,width=Width*0.24,height=Height*0.7)

    # noise_reduction_check
    font_  = ('Lexend','10')
    checkvar1 = IntVar()
    noise_reduction_check = Checkbutton(model_training_frame,text= "Noise Reduction", variable=checkvar1,font=font_,onvalue=1, offvalue=0) 
    noise_reduction_check.place(x=Width*0.01,y=Height*0.02,width=Width*0.09,height=Height*0.03)

    # skull_stripping
    font_  = ('Lexend','10')
    checkvar2 = IntVar()
    skull_stripping_check = Checkbutton(model_training_frame,text= "Skull Stripping", variable=checkvar2,font=font_,onvalue=1, offvalue=0) 
    skull_stripping_check.place(x=Width*0.01,y=Height*0.06,width=Width*0.08,height=Height*0.03)
    
    #data_preprocessing_status_label
    data_preprocessing_status_label = Label(model_training_frame,justify=LEFT,bd=0,text='Data Preprocessing Status :',fg='black',bg='#f0f0f0',font=('Lexend','8'))
    data_preprocessing_status_label.place(x=Width*0.01,y=Height*0.167,width=Width*0.11,height=Height*0.03)
    #data_preprocessing_status_entry
    data_preprocessing_status_entry = Entry(model_training_frame,justify=RIGHT,bd=0,fg='red',bg='#f0f0f0',font=('Lexend','8'), state='readonly')
    data_preprocessing_status_entry.place(x=Width*0.175,y=Height*0.167,width=Width*0.05,height=Height*0.03)
    data_preprocessing_status_entry.insert(0,'')

    # rotation
    font_  = ('Lexend','10')
    checkvar3 = IntVar()
    rotation_check = Checkbutton(model_training_frame,text= "Rotation", variable=checkvar3,font=font_,onvalue=1, offvalue=0) 
    rotation_check.place(x=Width*0.01,y=Height*0.21,width=Width*0.06,height=Height*0.03)

    # scaling
    font_  = ('Lexend','10')
    checkvar4 = IntVar()
    scaling_check = Checkbutton(model_training_frame,text= "Scaling", variable=checkvar4,font=font_,onvalue=1, offvalue=0) 
    scaling_check.place(x=Width*0.01,y=Height*0.25,width=Width*0.053,height=Height*0.03)

    # noise injection
    font_  = ('Lexend','10')
    checkvar5 = IntVar()
    noise_injection_check = Checkbutton(model_training_frame,text= "Noise Injection", variable=checkvar5,font=font_,onvalue=1, offvalue=0) 
    noise_injection_check.place(x=Width*0.01,y=Height*0.29,width=Width*0.09,height=Height*0.03)

    #data_augmentation_status_label
    data_augmentation_status_label = Label(model_training_frame,justify=LEFT,bd=0,text='Data Augmentation Status :',fg='black',bg='#f0f0f0',font=('Lexend','8'))
    data_augmentation_status_label.place(x=Width*0.01,y=Height*0.41,width=Width*0.11,height=Height*0.03)
    #data_augmentation_status_entry
    data_augmentation_status_entry = Entry(model_training_frame,justify=RIGHT,bd=0,fg='red',bg='#f0f0f0',font=('Lexend','8'), state='readonly')
    data_augmentation_status_entry.place(x=Width*0.175,y=Height*0.41,width=Width*0.05,height=Height*0.03)
    data_augmentation_status_entry.insert(0,'')


    #model_training_status_label
    model_training_status_entry = Label(model_training_frame,justify=LEFT,bd=0,text='Model Training Status :',fg='black',bg='#f0f0f0',font=('Lexend','8'))
    model_training_status_entry.place(x=Width*0.01,y=Height*0.535,width=Width*0.1,height=Height*0.03)
    #model_training_status_entry
    model_training_status_entry = Entry(model_training_frame,justify=RIGHT,bd=0,fg='red',bg='#f0f0f0',font=('Lexend','8'), state='readonly')
    model_training_status_entry.place(x=Width*0.175,y=Height*0.535,width=Width*0.05,height=Height*0.03)
    model_training_status_entry.insert(0,'')



    # frame 2
    # training_performance_measures_frame
    font_  = ('Lexend','9','bold') #A3BFD9
    training_performance_measures_frame = LabelFrame(mainframe,bg='#f0f0f0',bd=2,font=font_,text='  Training Performance Measures  ')
    training_performance_measures_frame.place(x=Width*0.275,y=Height*0.21,width=Width*0.43,height=Height*0.7)

    # 01
    # accuracy_label
    font_  = ('Lexend','9','bold')
    accuracy_label = Label(training_performance_measures_frame,text='Accuracy :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    accuracy_label.place(x=Width*0.01,y=Height*0.024,width=Width*0.19,height=Height*0.03)

    #accuracy_label_design
    accuracy_label_design = Label(training_performance_measures_frame,bd=2,bg='black')
    accuracy_label_design.place(x=Width*0.01,y=Height*0.057,width=Width*0.19,height=Height*0.003)

    #accuracy_entry
    accuracy_entry = Entry(training_performance_measures_frame,justify=LEFT,bd=0,fg='black',bg='#f0f0f0',font=('Lexend','18'), state='readonly')
    accuracy_entry.place(x=Width*0.01,y=Height*0.06,width=Width*0.19,height=Height*0.05)
    accuracy_entry.insert(0,'0.00000')

    # 02
    # precision_label
    font_  = ('Lexend','9','bold')
    precision_label = Label(training_performance_measures_frame,text='Precision :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    precision_label.place(x=Width*0.225,y=Height*0.024,width=Width*0.19,height=Height*0.03)

    #precision_label_design
    precision_label_design = Label(training_performance_measures_frame,bd=2,bg='black')
    precision_label_design.place(x=Width*0.225,y=Height*0.057,width=Width*0.19,height=Height*0.003)

    #precision_entry
    precision_entry = Entry(training_performance_measures_frame,justify=LEFT,bd=0,fg='black',bg='#f0f0f0',font=('Lexend','18'), state='readonly')
    precision_entry.place(x=Width*0.225,y=Height*0.06,width=Width*0.19,height=Height*0.05)
    precision_entry.insert(0,'0.00000')

    # 03
    # recall_label
    font_  = ('Lexend','9','bold')
    recall_label = Label(training_performance_measures_frame,text='Recall :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    recall_label.place(x=Width*0.01,y=Height*0.13,width=Width*0.19,height=Height*0.03)

    #recall_label_design
    recall_label_design = Label(training_performance_measures_frame,bd=2,bg='black')
    recall_label_design.place(x=Width*0.01,y=Height*0.163,width=Width*0.19,height=Height*0.003)

    #recall_entry
    recall_entry = Entry(training_performance_measures_frame,justify=LEFT,bd=0,fg='black',bg='#f0f0f0',font=('Lexend','18'), state='readonly')
    recall_entry.place(x=Width*0.01,y=Height*0.166,width=Width*0.19,height=Height*0.05)
    recall_entry.insert(0,'0.00000')

    # 04
    # f1_measure_label
    font_  = ('Lexend','9','bold')
    f1_measure_label = Label(training_performance_measures_frame,text='F1 Measure :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    f1_measure_label.place(x=Width*0.225,y=Height*0.13,width=Width*0.19,height=Height*0.03)

    #f1_measure_label_design
    f1_measure_label_design = Label(training_performance_measures_frame,bd=2,bg='black')
    f1_measure_label_design.place(x=Width*0.225,y=Height*0.163,width=Width*0.19,height=Height*0.003)

    #f1_measure_entry
    f1_measure_entry = Entry(training_performance_measures_frame,justify=LEFT,bd=0,fg='black',bg='#f0f0f0',font=('Lexend','18'), state='readonly')
    f1_measure_entry.place(x=Width*0.225,y=Height*0.166,width=Width*0.19,height=Height*0.05)
    f1_measure_entry.insert(0,'0.00000')

    # 04
    # confusin_matrix_label
    font_  = ('Lexend','9','bold')
    confusin_matrix_label = Label(training_performance_measures_frame,text='Confusion Matrix :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    confusin_matrix_label.place(x=Width*0.01,y=Height*0.23,width=Width*0.19,height=Height*0.03)

    #confusin_matrix_label_design
    confusin_matrix_label_design = Label(training_performance_measures_frame,bd=2,bg='black')
    confusin_matrix_label_design.place(x=Width*0.01,y=Height*0.263,width=Width*0.405,height=Height*0.003)

    # confusion_matrix_entry_label
    confusion_matrix_entry_label = Label(training_performance_measures_frame,fg='white',text='Confusion Matrix Image',bg='black',bd=0)
    confusion_matrix_entry_label.place(x=Width*0.01,y=Height*0.28,width=Width*0.405,height=Height*0.375)


    # frame 3
    # evaluation_performance_measures_frame
    font_  = ('Lexend','9','bold')
    evaluation_performance_measures_frame = LabelFrame(mainframe,bg='#f0f0f0',bd=2,font=font_,text='  Evaluation Performance Measures  ')
    evaluation_performance_measures_frame.place(x=Width*0.715,y=Height*0.21,width=Width*0.24,height=Height*0.7)

    # upload_image_label
    font_  = ('Lexend','9','bold')
    upload_image_label = Label(evaluation_performance_measures_frame,text='Upload MRI/CT Scan Image :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    upload_image_label.place(x=Width*0.01,y=Height*0.034,width=Width*0.14,height=Height*0.03)


    #upload_image_status_entry
    upload_image_status_entry = Entry(evaluation_performance_measures_frame,justify=RIGHT,bd=0,fg='red',bg='#f0f0f0',font=('Lexend','8'), state='readonly')
    upload_image_status_entry.place(x=Width*0.01,y=Height*0.075,width=Width*0.215,height=Height*0.04)
    upload_image_status_entry.insert(0,'No MRI CT Scan Image Found!')

    # image_entry [image will be shown within this label]
    image_entry = Label(evaluation_performance_measures_frame,bg='white',bd=0)
    image_entry.place(x=Width*0.01,y=Height*0.125,width=Width*0.215,height=Height*0.28)

    # 01
    # evaluation_status_label
    font_  = ('Lexend','9','bold')
    evaluation_status_label = Label(evaluation_performance_measures_frame,text='Tumor Status :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    evaluation_status_label.place(x=Width*0.01,y=Height*0.47,width=Width*0.19,height=Height*0.03)

    #evaluation_status_label_design
    evaluation_status_label_design = Label(evaluation_performance_measures_frame,bd=2,bg='black')
    evaluation_status_label_design.place(x=Width*0.01,y=Height*0.503,width=Width*0.215,height=Height*0.003)

    #evaluation_status_entry
    evaluation_status_entry = Entry(evaluation_performance_measures_frame,justify=LEFT,bd=0,fg='red',bg='#f0f0f0',font=('Lexend','14'), state='readonly')
    evaluation_status_entry.place(x=Width*0.01,y=Height*0.506,width=Width*0.215,height=Height*0.05)
    evaluation_status_entry.insert(0,'Tumor Found!')

    # 02
    # evaluation_accuracy_label
    font_  = ('Lexend','9','bold')
    evaluation_accuracy_label = Label(evaluation_performance_measures_frame,text='Evaluation Accuracy :',font=font_,fg='black',bg='#f0f0f0',bd=0,justify=LEFT,anchor='w')
    evaluation_accuracy_label.place(x=Width*0.01,y=Height*0.56,width=Width*0.19,height=Height*0.03)

    #evaluation_accuracy_label_design
    evaluation_accuracy_label_design = Label(evaluation_performance_measures_frame,bd=2,bg='black')
    evaluation_accuracy_label_design.place(x=Width*0.01,y=Height*0.593,width=Width*0.215,height=Height*0.003)

    #evaluation_accuracy_label_entry
    evaluation_accuracy_label_entry = Entry(evaluation_performance_measures_frame,justify=LEFT,bd=0,fg='black',bg='#f0f0f0',font=('Lexend','18'), state='readonly')
    evaluation_accuracy_label_entry.place(x=Width*0.01,y=Height*0.596,width=Width*0.215,height=Height*0.05)
    evaluation_accuracy_label_entry.insert(0,'0.00000')





    # FUNCTIONS
    #upload_dataset_fn
    def upload_dataset_fn():
        global input_dir
        
        input_dir = os.path.normpath(filedialog.askdirectory())
        if not input_dir:
            return
        
        print("Input Directory: " + input_dir)
        
        folder_path_yes = os.path.join(input_dir, 'yes')
        folder_path_no = os.path.join(input_dir, 'no')
        
        images_no = 0
        
        if os.path.exists(folder_path_yes):
            # Get list of image files from the selected folder
            image_files = [f for f in os.listdir(folder_path_yes) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            images_no = len(image_files)
            
            if image_files:
                # Display the first image from the folder
                file_path = os.path.join(folder_path_yes, image_files[0])
                # loginscreen_image (use PIL library) -> access image from the system
                img = Image.open(file_path)
                # resize the image and apply a high-quality down sampling filter
                img = img.resize((int(Width*0.14),int(Width*0.14)), Image.Resampling.LANCZOS)
                # PhotoImage class is used to add image to widgets, icons etc
                final_image = ImageTk.PhotoImage(img)
        else:
            show_warning("'yes' folder not found!")    
            return     
        if os.path.exists(folder_path_no):
            # Get list of image files from the selected folder
            image_files = [f for f in os.listdir(folder_path_no) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            images_no += len(image_files)
        else:
            show_warning("'no' folder not found!")
            return
        path_entry.config(state='normal')
        path_entry.delete(0,END)
        path_entry.insert(0,input_dir)
        path_entry.config(state='readonly')
        
        dataset_status_entry.config(state='normal')
        dataset_status_entry.delete(0,END)
        dataset_status_entry.insert(0,'{} Images Uploaded!'.format(images_no))
        dataset_status_entry.config(state='readonly')

    #upload_dataset_button
    font_  = ('Lexend','9','bold')
    upload_dataset_button = Button(mainframe,text='Upload',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=upload_dataset_fn,activebackground='white',activeforeground='black', cursor='hand2')
    upload_dataset_button.place(x=Width*0.12,y=Height*0.148,width=Width*0.055,height=Height*0.04)

    #upload_image_fn
    def upload_image_fn():
        global input_image_for_evaluation
        # Open file dialog box and get the image file path
        input_image_for_evaluation = os.path.normpath(filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")]))
        if input_image_for_evaluation:
            # loginscreen_image (use PIL library) -> access image from the system
            img = Image.open(input_image_for_evaluation)
            # resize the image and apply a high-quality down sampling filter
            img = img.resize((int(Width*0.14),int(Width*0.14)), Image.Resampling.LANCZOS)
            # PhotoImage class is used to add image to widgets, icons etc
            final_image = ImageTk.PhotoImage(img)

            # Set the image in the label
            image_entry.config(image=final_image)
            image_entry.image = final_image

            upload_image_status_entry.delete(0,END)
            upload_image_status_entry.insert(0,'MRI CT Scan Uploaded!')

    #upload_image_button
    font_  = ('Lexend','9','bold')
    upload_image_button = Button(evaluation_performance_measures_frame,text='Upload',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=upload_image_fn,activebackground='white',activeforeground='black', cursor='hand2')
    upload_image_button.place(x=Width*0.162,y=Height*0.028,width=Width*0.06,height=Height*0.04)

    def start_evaluate_tumor():
        thread = threading.Thread(target=evaluate_tumor_thread)
        thread.start()
        
    def evaluate_tumor_thread():
        global input_dir
        global input_image_for_evaluation
        
        # Dataset selection validation
        if not input_dir:
            show_error('Dataset is not selected!\nDataset directory is necessary for picking up the model!')
            return
        
        # Check for model file
        model_path = os.path.join(os.path.join(os.path.dirname(input_dir), 'model'), 'brain_tumor_detection.keras')
        if not os.path.exists(model_path):
            show_error('Model is not available!\n Please do model training first!')
            return

        # Image selection validation
        if not input_image_for_evaluation:
            show_error('Image is not selected!')
            return
        
        evaluation_status_entry.config(state='normal')
        evaluation_accuracy_label_entry.config(state='normal')
        
        evaluation_status_entry.delete(0, END)
        evaluation_accuracy_label_entry.delete(0, END)
        
        evaluation_status_entry.insert(0, 'Computing...')
        evaluation_accuracy_label_entry.insert(0, 'Computing...')
    
        from predict import predict_tumor
        result, accuracy_confidence = predict_tumor(input_image_for_evaluation, model_path)
        
        if result and accuracy_confidence:
            
            evaluation_status_entry.delete(0, END)
            evaluation_accuracy_label_entry.delete(0, END)
            
            evaluation_status_entry.insert(0, result)
            evaluation_accuracy_label_entry.insert(0, f"{accuracy_confidence:.5f}")
            
            evaluation_status_entry.config(state='readonly')
            evaluation_accuracy_label_entry.config(state='readonly')
        else:
            evaluation_status_entry.delete(0, END)
            evaluation_accuracy_label_entry.delete(0, END)
            
            evaluation_status_entry.insert(0, 'Failed!')
            evaluation_accuracy_label_entry.insert(0, 'Failed!')
            
            evaluation_status_entry.config(state='readonly')
            evaluation_accuracy_label_entry.config(state='readonly')
        
    #evaluate_button
    font_  = ('Lexend','9','bold')
    evaluate_button = Button(evaluation_performance_measures_frame,text='Evaluate Tumor',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=start_evaluate_tumor,activebackground='white',activeforeground='black', cursor='hand2')
    evaluate_button.place(x=Width*0.01,y=Height*0.42,width=Width*0.215,height=Height*0.04)

    #data_preprocessing
    def data_preprocessing_callback(processed, total):
        data_preprocessing_status_entry.delete(0, END)
        data_preprocessing_status_entry.insert(0, f"{processed}/{total}")
        mainframe.update_idletasks()
    
    def start_data_preprocessing():
        thread = threading.Thread(target=data_preprocessing_thread)
        thread.start()
        
    def data_preprocessing_thread():
        global input_dir
        # Dataset selection validation
        if not input_dir:
            show_error('Dataset is not selected!')
            return
        
        # Options validation
        noise_reduction = bool(checkvar1.get())
        skull_strip = bool(checkvar2.get())
        
        if not noise_reduction and not skull_strip:
            show_warning('Please select at least one preprocessing technique!')
            return
        
        # Data Augmentation Validation
        data_augment_status = data_augmentation_status_entry.get()
        augmented_data_path = os.path.join(input_dir, 'augmented_data')
            
        if data_augment_status == 'Done!':
            show_warning('Data Augmentation has already been done!\nYou have to do Data Augmentation again after Data Preprocessing')
        elif data_augment_status != '' and data_augment_status != 'Done!':
            show_error('Data Augmentation is being done!\nWait until Data Augmentation is done.')
            return
        else:
            pass
        
        if os.path.exists(augmented_data_path):
            os.system(f'rmdir "{augmented_data_path}" /s /q')
            print("Previous data_augmented directory found and deleted!")
            
        data_preprocessing_status_entry.config(state='normal')
        data_preprocessing_status_entry.delete(0, END)
        data_preprocessing_status_entry.insert(0, "Processing...")
        
        from data_pre_processing import pre_process_data
        
        yes_dir_path = os.path.join(input_dir, "yes")
        no_dir_path = os.path.join(input_dir, "no")
        
        pre_process_data([yes_dir_path, no_dir_path], noise_reduction, skull_strip, update_callback=data_preprocessing_callback)
        
        data_preprocessing_status_entry.delete(0, END)
        data_preprocessing_status_entry.insert(0, "Done!")
        data_preprocessing_status_entry.config(state='readonly')
        
        
    #data_preprocessing_button
    font_  = ('Lexend','10','bold')
    data_preprocessing_button = Button(model_training_frame,text='Data Preprocessing',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=start_data_preprocessing,activebackground='white',activeforeground='black', cursor='hand2')
    data_preprocessing_button.place(x=Width*0.01,y=Height*0.105,width=Width*0.215,height=Height*0.06) 
    
    def data_augment_update_progress(processed, total):
        data_augmentation_status_entry.delete(0, END)
        data_augmentation_status_entry.insert(0, f"{processed}/{total}")
        mainframe.update_idletasks() 
    
    def on_perform_data_augmentation():
        # Start the data augmentation process in a separate thread
        thread = threading.Thread(target=perform_data_augmentation_thread)
        thread.start()

    def perform_data_augmentation_thread():
        global input_dir
        
        if not input_dir:
            show_error('Dataset is not selected!')
            return
        
        data_pre_processing_status = data_preprocessing_status_entry.get()
        if data_pre_processing_status != '' and data_pre_processing_status != 'Done!':
            show_error('Data Pre-Processing is being done!\nWait until Data Pre-Processing is done.')
            return
        
        # Get the values of the checkboxes
        rotation = bool(checkvar3.get()) 
        scaling = bool(checkvar4.get())
        noise_injection = bool(checkvar5.get())
        
        if not rotation and not scaling and not noise_injection:
            show_warning('No transformations selected!')
            return
        data_augmentation_status_entry.config(state='normal')
        data_augmentation_status_entry.delete(0, END)
        data_augmentation_status_entry.insert(0, 'Processing...')
        mainframe.update_idletasks()
        
        if os.path.exists(os.path.join(input_dir, 'pre_processed_data')):
            pre_processed_dir = os.path.join(input_dir, 'pre_processed_data')
        
        from data_augmentation import perform_data_augmentation
        perform_data_augmentation(
            file_dir=pre_processed_dir,   
            update_callback=data_augment_update_progress,             
            rotation=rotation,
            scaling=scaling,
            noise_injection=noise_injection
        )
        
        # Update the status entry
        data_augmentation_status_entry.delete(0, END)
        data_augmentation_status_entry.insert(0, 'Done!')
        data_augmentation_status_entry.config(state='readonly')
    
    #data_augmentaion_button
    font_  = ('Lexend','10','bold')
    data_augmentaion_button = Button(model_training_frame,text='Data Augmentation',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=on_perform_data_augmentation,activebackground='white',activeforeground='black', cursor='hand2')
    data_augmentaion_button.place(x=Width*0.01,y=Height*0.348,width=Width*0.215,height=Height*0.06)
    
    def model_training_callback(completed_epochs, total):
        model_training_status_entry.delete(0, END)
        if 'evaluating' not in str(completed_epochs):
            model_training_status_entry.insert(0, f"{completed_epochs}/{total}")
        else:
            model_training_status_entry.insert(0, f"{completed_epochs}")
            
        mainframe.update_idletasks()
    
    def start_model_training():
        thread = threading.Thread(target=model_training_thread)
        thread.start()
        
    def model_training_thread():
        global input_dir
        
        # Dataset selection validation
        if not input_dir:
            show_error('Dataset is not selected!')
            return
        
        # Validations 
        data_augment_status = data_augmentation_status_entry.get()
        if data_augment_status != '' and data_augment_status != "Done!":
            show_error('Data Augmentation is being done!\nWait until Data Augmentation is done.')
            return
        
        data_pre_processing_status = data_preprocessing_status_entry.get()
        if data_pre_processing_status != '' and data_pre_processing_status != 'Done!':
            show_error('Data Pre-Processing is being done!\nWait until Data Pre-Processing is done.')
            return
        
        model_training_status_entry.config(state='normal')
        model_training_status_entry.delete(0, END)
        model_training_status_entry.insert(0, 'Processing...')
        mainframe.update_idletasks()
            
        processed_input_dir = None
        if os.path.exists(os.path.join(input_dir, 'augmented_data')):
            processed_input_dir = os.path.join(input_dir, 'augmented_data')    
        elif os.path.exists(os.path.join(input_dir, 'pre_processed_data')):
            processed_input_dir = os.path.join(input_dir, 'pre_processed_data')
        else:
            pass
        
        if processed_input_dir is not None:
            yes_dir_path = os.path.join(processed_input_dir, "yes")
            no_dir_path = os.path.join(processed_input_dir, "no")
        else:
            yes_dir_path = os.path.join(input_dir, "yes")
            no_dir_path = os.path.join(input_dir, "no")
        
        from model import model_training
        model_training(input_dir, [yes_dir_path, no_dir_path], update_epoch_progress=model_training_callback)
        
        # Update the status entry
        model_training_status_entry.delete(0, END)
        model_training_status_entry.insert(0, 'Done!')
        model_training_status_entry.config(state='readonly')
        
        
    #model_training_button
    font_  = ('Lexend','10','bold')
    model_training_button = Button(model_training_frame,text='Model Training',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=start_model_training,activebackground='white',activeforeground='black', cursor='hand2')
    model_training_button.place(x=Width*0.01,y=Height*0.47,width=Width*0.215,height=Height*0.06)
    
    
    
    def start_performance_measurment():
        thread = threading.Thread(target=performance_measurment_thread)
        thread.start()
        
    def performance_measurment_thread():
        global input_dir
        
        # Dataset selection validation
        if not input_dir:
            show_error('Dataset is not selected!\nDataset directory is necessary for picking up the model!')
            return
        
        # Check for model evaluation file
        main_dir = os.path.dirname(input_dir)
        if not os.path.exists(os.path.join(main_dir, 'model_evaluation')):
            show_error('Model is not available!\n Please do model training first!')
            return
        
        accuracy_entry.config(state='normal')
        precision_entry.config(state='normal')
        recall_entry.config(state='normal')
        f1_measure_entry.config(state='normal')
        
        accuracy_entry.delete(0, END)
        precision_entry.delete(0, END)
        recall_entry.delete(0, END)
        f1_measure_entry.delete(0, END)
        
        accuracy_entry.insert(0, "Computing...")
        precision_entry.insert(0, "Computing...")
        recall_entry.insert(0, "Computing...")
        f1_measure_entry.insert(0, "Computing...")
        
        
        from model import read_performance_metrics, display_confusion_matrix
        
        conf_matrix_img_path = os.path.join(os.path.join(main_dir, 'model_evaluation'), 'confusion_matrix.png')
        
        try:
            metrics = None
            if not os.path.exists(conf_matrix_img_path):    
                metrics = read_performance_metrics(os.path.join(main_dir, 'model_evaluation'), conf_matrix_image=True)
            else:
                metrics = read_performance_metrics(os.path.join(main_dir, 'model_evaluation'))
                
            if not metrics:
                accuracy_entry.delete(0, END)
                precision_entry.delete(0, END)
                recall_entry.delete(0, END)
                f1_measure_entry.delete(0, END)
                
                accuracy_entry.insert(0, "0.00000")
                precision_entry.insert(0, "0.00000")
                recall_entry.insert(0, "0.00000")
                f1_measure_entry.insert(0, "0.00000")
                
                accuracy_entry.config(state='readonly')
                precision_entry.config(state='readonly')
                recall_entry.config(state='readonly')
                f1_measure_entry.config(state='readonly')
                return
            
            accuracy, precision, recall, f1_measure, conf_matrix = metrics
            display_confusion_matrix(conf_matrix_img_path, confusion_matrix_entry_label)
            
            accuracy_entry.delete(0, END)
            precision_entry.delete(0, END)
            recall_entry.delete(0, END)
            f1_measure_entry.delete(0, END)
            
            accuracy_entry.insert(0, f"{accuracy:.5f}")
            precision_entry.insert(0, f"{precision:.5f}")
            recall_entry.insert(0, f"{recall:.5f}")
            f1_measure_entry.insert(0, f"{f1_measure:.5f}")
            
            accuracy_entry.config(state='readonly')
            precision_entry.config(state='readonly')
            recall_entry.config(state='readonly')
            f1_measure_entry.config(state='readonly')
            
            
        except:
            accuracy_entry.delete(0, END)
            precision_entry.delete(0, END)
            recall_entry.delete(0, END)
            f1_measure_entry.delete(0, END)
            
            accuracy_entry.insert(0, "0.00000")
            precision_entry.insert(0, "0.00000")
            recall_entry.insert(0, "0.00000")
            f1_measure_entry.insert(0, "0.00000")
            
            accuracy_entry.config(state='readonly')
            precision_entry.config(state='readonly')
            recall_entry.config(state='readonly')
            f1_measure_entry.config(state='readonly')
            return
            
        
    #performance_measures_button
    font_  = ('Lexend','10','bold')
    performance_measures_button = Button(model_training_frame,text='Performance Measures',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=start_performance_measurment,activebackground='white',activeforeground='black', cursor='hand2')
    performance_measures_button.place(x=Width*0.01,y=Height*0.592,width=Width*0.215,height=Height*0.06)


    # RESET FUNCTION
    def reset_fn_():
        path_entry.config(state='normal')
        dataset_status_entry.config(state='normal')
        data_preprocessing_status_entry.config(state='normal')
        data_augmentation_status_entry.config(state='normal')
        model_training_status_entry.config(state='normal')
        accuracy_entry.config(state='normal')
        precision_entry.config(state='normal')
        recall_entry.config(state='normal')
        f1_measure_entry.config(state='normal')
        upload_image_status_entry.config(state='normal')
        evaluation_status_entry.config(state='normal')
        evaluation_accuracy_label_entry.config(state='normal')
        
        path_entry.delete(0,END)
        dataset_status_entry.delete(0,END)
        data_preprocessing_status_entry.delete(0,END)
        data_augmentation_status_entry.delete(0,END)
        model_training_status_entry.delete(0,END)
        accuracy_entry.delete(0,END)
        precision_entry.delete(0,END)
        recall_entry.delete(0,END)
        f1_measure_entry.delete(0,END)
        upload_image_status_entry.delete(0,END)
        evaluation_status_entry.delete(0,END)
        evaluation_accuracy_label_entry.delete(0,END)
        
        path_entry.config(state='readonly')
        dataset_status_entry.config(state='readonly')
        data_preprocessing_status_entry.config(state='readonly')
        data_augmentation_status_entry.config(state='readonly')
        model_training_status_entry.config(state='readonly')
        accuracy_entry.config(state='readonly')
        precision_entry.config(state='readonly')
        recall_entry.config(state='readonly')
        f1_measure_entry.config(state='readonly')
        upload_image_status_entry.config(state='readonly')
        evaluation_status_entry.config(state='readonly')
        evaluation_accuracy_label_entry.config(state='readonly')

        # remove image
        image_entry.config(image='')
        image_entry.image = None
        upload_image_status_entry.insert(0,'No MRI CT Scan Image Found!')
        
        confusion_matrix_entry_label.config(image='')
        confusion_matrix_entry_label.image = None
        confusion_matrix_entry_label.config(bg='black', text='Confusion Matrix Image')
        
    #reset_button
    font_  = ('Lexend','12','bold')
    reset_button = Button(mainframe,text='Reset',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=reset_fn_,activebackground='white',activeforeground='black', cursor='hand2')
    reset_button.place(x=Width*0.745,y=Height*0.033,width=Width*0.1,height=Height*0.065)


    # LOGOUT FUNCTION
    def logout_fn_():
        # clear the previous frame
        for widgets in mainframe.winfo_children():
            widgets.destroy()

        from login import login_fn
        login_fn(loginscreen_image,mainframe,Width,Height)

    #logout_button
    font_  = ('Lexend','12','bold')
    logout_button = Button(mainframe,text='Logout',font=font_,fg='black',bg='#A3BFD9',bd=0,justify=CENTER,
                             command=logout_fn_,activebackground='white',activeforeground='black', cursor='hand2')
    logout_button.place(x=Width*0.855,y=Height*0.033,width=Width*0.1,height=Height*0.065)
    
    
# General Methods
def show_warning(msg):
    messagebox.showwarning("Warning", msg)
    
def show_error(msg):
    messagebox.showerror("Error", msg)