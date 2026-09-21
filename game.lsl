load random as r

secret_number = r.randint(1, 1000)
invalid_attempts = 0

loop:
    user_input = input "Your guess: "

    try:
        guess = Int(user_input.strip())

    else:
        invalid_attempts += 1
        if invalid_attempts >= 5:
            print "Too many invalid inputs, ending."
            break
        end
        print "That is not a whole number, try again."
        continue
    end

    invalid_attempts = 0

    if secret_number < guess:
        print "Too big!"

    elif secret_number > guess:
        print "Too small!"

    else:
        print "Correct!"
        break
    end
end

print l"Correct number was {secret_number}"

# Note:
# For running this code, you can download compliler for Linux x86 here:
# https://lsl.lux-ai.cz/
