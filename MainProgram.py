import label_image


while(True):
    print('==========================================')
    print('Welcome to Data Virtual Assitant')
    print('------------------------------------------')
    print('1.Log In')
    print('2.Create a account')
    print('3.Exit')
    print('------------------------------------------')
    print('==========================================')
    c = int(input('Choose your option:'))
    if(c==1):
        label_image.main()
    elif(c==2):
        import crop_image_creating_admin
        print('Please Wait untill training stop.')
        from subprocess import Popen
        p = Popen(['python','retrain.py'])
    elif(c==3):
        break
    else:
        print('Wrong input Try Again')
