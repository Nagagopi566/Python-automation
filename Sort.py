self.student_dict = {}
with open(filename, 'r') as file: 
    for line in file:
        name, height = line.strip().split(',')
        self.student_dict[name] = float(height)
        sorted_dict = dict(self.student_dict)
        keys = list(sorted_dict.keys())
        for i in range(1, len(keys)):
            current_key = keys[i]
            current_height = sorted_dict[current_key]
            j = i - 1
            while j >= 0 and current_height > sorted_dict[keys[j]]:
                keys[j + 1] = keys[j]
                j -= 1
            keys[j + 1] = current_key
      return {key: sorted_dict[key] for key in keys}
        with open(filename, 'w') as file:
            for name, height in self.student_dict.items():
                file.write(f"Name: {name}, Height: {height} \n")
            print("Sorted data saved to file.")
            sorted_students = self.insertion_sort_by_height()
            self.student_dict = sorted_storter()

 

# Get student data from input file, sort by height using insertion sort, and save sorted data to output file
input_filename = "input.txt"
output_filename = "output.txt"
