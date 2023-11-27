try:
    data = open('missing.txt')
    print(data.redline(),end='')
except IOError as err:
    print("File error: " + str(err))
finally:
    if 'data' in locals():
        data.close()
    