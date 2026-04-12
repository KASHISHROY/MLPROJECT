import sys   ##any exception that happens sys library will have the information
from src.logger import logging


##whenever error raised call this particular function

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]" .format(
        file_name,exc_tb.tb_lineno,str(error)
    
    )
    return error_message

class CustomException(Exception):
    #3constructor initialized
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message


##this is common wherever u ll be using try catch and inside try and exception is raised it will show that error raise on file so and so line number so and so


