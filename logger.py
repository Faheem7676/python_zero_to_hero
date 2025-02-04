# import datetime

# class logger:
    
#     """A simple logging mechanism that supports different logging levels.
#     """

#     LEVELS= {"info": "INFO",
#            "Warning": "Warning",
#            "Error":  "Error"
#            }
    
#     print(LEVELS)
    
    
#     def __init__(self,log_file=None):
#         """initalize the logger with an optional log file.
        
#         : parameter log_file: path to the log file (default:None prints to console).
#         """
        
#         self.log_file=log_file
        
#     def log(self,level,message):
#         """Logs a message with a given level.
#         : Param level : Log level (INFO, Warning, Error)
#         : Parma message: Log message
#         """
        
#         if level not in self.LEVELS:
#             raise ValueError("Invalid log level")
        
#         log_entry=f"[{datetime.datetime.now()}] {level}: {message}"
        
#         if self.log_file:
#             with open(self.log_file,'a') as file:
                
#                 file.write(log_entry + '\n')
                
#         else:
#             print(log_entry)
    
#     def info(self,message):
        
#         self.log(self.LEVELS["INFO"],message)
        
#     def warning(self,message):
        
#         self.log(self.LEVELS["WARNING"],message) 
        
#     def error(self,message):
        
#         self.log(self.LEVELS["ERROR"],message)
        
        
# obj=logger()
# print(obj.log("INFO","it is high periority"))
# print(obj.info("This is info message"))
# print(obj.warning("This is wrning message"))
# print(obj.error("This is an error message"))



import datetime

class Logger:
    """A simple logging mechanism that supports different logging levels."""
    
    LEVELS = {
        "INFO": "INFO",
        "WARNING": "WARNING",
        "ERROR": "ERROR"
    }
    
    def __init__(self, log_file=None):
        """Initialize the logger with an optional log file.
        
        :param log_file: Path to the log file (default: None prints to console).
        """
        self.log_file = log_file

    def log(self, level, message):
        """Logs a message with a given level.
        
        :param level: Log level (INFO, WARNING, ERROR)
        :param message: Log message
        """
        if level not in self.LEVELS:
            raise ValueError("Invalid log level")
        
        log_entry = f"[{datetime.datetime.now()}] {level}: {message}"
        
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(log_entry + '\n')
        else:
            print(log_entry)
    
    def info(self, message):
        """Logs an INFO message."""
        self.log(self.LEVELS["INFO"], message)
        
    def warning(self, message):
        """Logs a WARNING message."""
        self.log(self.LEVELS["WARNING"], message) 
        
    def error(self, message):
        """Logs an ERROR message."""
        self.log(self.LEVELS["ERROR"], message)


# Example usage
logger = Logger()

# Corrected method calls
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")

# Corrected log call with valid level
logger.log("INFO", "This is a direct log call.")
