row1 = ['😗', '😙', '😚']
row2 = ['🥰', '😍', '🤪']
row3 = ['😤', '😡', '🤯']

matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter the position to know my mood on you right now 🤨 ")
row_number = int(position[0])
column_number = int(position[1])
row = matrix[row_number-1]
row[column_number-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
