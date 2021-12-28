from website import create_app

app = create_app()
# this block executes only 
# when this file is directly run
if __name__ == '__main__':  #App runs only ifyou run this file
     # starts a web server    
     # the server is re-run automatically if 
     # there's some changes in the python code 
     app.run(debug=True)
