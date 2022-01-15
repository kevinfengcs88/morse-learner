def auto_type(morse, action, key):
    action.pause(1)
    for char in morse:
        match char:
            case '.':
                action.click(on_element=key)
                action.perform()
                print(".", end="")
            case '-':
                action.click_and_hold(on_element=key)
                action.release(on_element=key)
                action.perform()
                print("-", end="")
            case ' ':
                action.pause(0.5)
                action.perform()
                print(" ", end="")
            case '/':
                action.pause(1)
                action.perform()
                print("/", end="")
