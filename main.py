def main():
    score = int(input('Enter your input: '))
    
    if score < 60:
        grade = 'F'
    elif score < 70:
        grade = 'D'
    elif score < 80:
        grade = 'C'
    elif score < 90:
        grade = 'B'
    else:
        grade = 'A'

    print(f'Score: {score} \t Grade: {grade}')

    ########################################
    # Do not delete the return statement
    ########################################
    return grade


if __name__ == '__main__':
    main()
