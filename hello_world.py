print(2**3)


#(cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#Traceback (most recent call last):
#  File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1, in <module>
#    prit("Hello, World!")
#    ^^^^
#NameError: name 'prit' is not defined. Did you mean: 'print'?


#(cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py      
#  File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
#   print("Hello, World!)
#        ^
#SyntaxError: unterminated string literal (detected at line 1)


#(cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#  File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
#    print("Hello, World!"
#         ^
#SyntaxError: '(' was never closed


# ERROR conda.cli.main_run:execute(127): `conda run python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py` failed. (See above for error)
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#   File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
    # print"")
        #    ^
# SyntaxError: unmatched ')'
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#   File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
    # print(Hello World)
        #   ^^^^^^^^^^^

# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# ERROR conda.cli.main_run:execute(127): `conda run python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py` failed. (See above for error)
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> 
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#   File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
    # print("Hello World"""")
                    #    ^

# SyntaxError: unterminated triple-quoted string literal (detected at line 38)
# ERROR conda.cli.main_run:execute(127): `conda run python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py` failed. (See above for error)
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> 
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> & conda run --live-stream --name cs2526 python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py
#   File "c:\Users\shlom\01-hello-world-and-error-hunt-blinky32123\hello_world.py", line 1
    # print("Hello World") what
                        #  ^^^^

# SyntaxError: invalid syntax
# ERROR conda.cli.main_run:execute(127): `conda run python c:/Users/shlom/01-hello-world-and-error-hunt-blinky32123/hello_world.py` failed. (See above for error)
# (cs2526) PS C:\Users\shlom\01-hello-world-and-error-hunt-blinky32123> 