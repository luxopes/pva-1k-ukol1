load random as r

a = r.randint(1, 1000)
spatne = 0

loop:
    text = input "Your guess: "
    try:
        b = Int(text.strip())
    else:
        spatne += 1
        if spatne >= 5:
            print "Too many invalid inputs, ending."
            break
        end
        print "That is not a whole number, try again."
        continue
    end
    spatne = 0

    if a < b:
        print "Too big!"
    elif a > b:
        print "Too small!"
    else:
        print "Correct!"
        break
    end
end

print l"Correct number was {a}"
