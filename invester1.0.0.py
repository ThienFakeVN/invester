print('Available languages: Vietnamese, English')
language = input('Choose a language: ')
if language.casefold() == 'vietnamese': exec(r"""
import random, os, json

'''
KỂ CẢ KHI ĐÂY LÀ TRÒ CHƠI MÃ NGUỒN MỞ, ĐÙNG CHỈNH SỬA MÃ CỦA TRÒ CHƠI
NÓ CÓ THỂ DẪN ĐẾN CÁC LỖI KHÔNG LƯỜNG TRƯỚC!
'''

print()
print('Bạn có 100 rúp Nga. Bạn định đi đầu tư.')
print('Chào mừng đến với \033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m!')

def action():
    print()
    command = None
    command = input('Nhập một lệnh, như "START" để bắt đầu trò chơi, "STORY" để xem cốt truyện hay "?" để xem danh sách lệnh: ')
    if command.casefold() == 'start': play()
    elif command.casefold() == 'story': print('''
Có 3 công ty:
    - Công ty \033[38;2;63;72;204mA\033[0m: Viết tắt của \033[38;2;63;72;204;4mA\033[38;2;63;72;204mđù\033[0m. Lãi và lỗ ít, thường ít lỗ hơn lãi;
    - Công ty \033[38;2;163;73;164mB\033[0m: Viết tắt của, ờ... \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m? Vâng, \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m. Lãi và lỗ trung bình;
    - Công ty \033[38;2;136;0;21mC\033[0m: Viết tắt của \033[38;2;136;0;21;4mC\033[38;2;136;0;21moin \033[38;2;136;0;21;4mC\033[38;2;136;0;21mard\033[0m. Lãi thì mua siêu xe còn lỗ thì bán nhà, tiếc là thường lỗ hơn lãi. Chắc thằng chủ tịch công ty này đem tiền đầu tư đi đánh lô.
Bạn sẽ mua cổ phần của các công ty này và bán chúng, thay đổi của tổng cổ phần các công ty sẽ ảnh hưởng đến túi tiền của bạn và ảnh hưởng bao nhiêu phụ thuộc và phần trăm cổ phần của các công ty mà bạn sở hứu.
(Và bạn không hề quan tâm đến việc điều hành công ty, nên mua bao nhiêu cổ phần thì bạn cũng không làm ảnh hưởng đến các quyết định của công ty)
Thêm nữa, nếu thu nhập của bạn quá nhiều thì chính quyền Xã hội Dân chủ sẽ thu thuế, nhưng bạn sẽ không được hỗ trợ tài chính nếu bạn hết tiền vì đơn giản, bạn không tạo ra gì cho xã hội cả, chỉ ngồi không và (cầu mong) được nhận tiền.
(Nói về hỗ trợ, nếu các công ty phá sản, họ cũng sẽ nhận được hỗ trợ tài chính)
Chúc 100 rúp Nga của bạn không bay màu!''')
    elif command.casefold() == 'help' or command.casefold() == '?' : print('''
ABOUTME/ABOUTUS     Hiển thị thông tin về tôi — người tạo ra trò chơi này
ABOUTUPDATE         Hiển thị thông tin về bản cập nhật này
CREDITS             Hiển thị thông tin về bên sản xuất trò chơi
CWD                 Hiển thị thư mục làm việc hiện tại
HELP/?              Hiển thị danh sách lệnh có thể sử dụng tại khu vực action
READ                Đọc một tệp .json chứa dữ liệu trò chơi
START               Bắt đầu trò chơi
STORY               Kể câu truyện trong trò chơi
UPDATE              Tìm và thay đổi bản cập nhật của trò chơi (yêu cầu mô đun requests)''')
    elif command.casefold() == 'cwd': print(f'''
Thư mục làm việc hiện tại: {os.getcwd()}. Đây cũng là nơi các tệp trò chơi sẽ được lưu nếu bạn chọn lưu chúng.''')
    elif command.casefold() == 'read': read()
    elif command.casefold() == 'aboutme' or command.casefold() == 'aboutus': print('''
Tôi tên là Thiện, bạn có thể gọi tôi là ThienFakeVN hoặc ThieenjVN.
Tôi (chỉ có mình tôi) là người đã tạo ra trò chơi này. Đây cũng là trò chơi đầu tiên tôi làm.
Tôi làm ra những trò chơi miễn phí và mã nguồn mở, sử dụng màn hình Terminal, được viết bằng Python, có nội dung là những thứ vừa đơn giản vừa phức tạp vừa đơn giản mà tôi nghĩ ra trong đầu.
Tài khoản GitHub cho ai cần: ThienFakeVN.''')
    elif command.casefold() == 'credits' or command.casefold() == 'credit': print('''
\033[1mCREDITS — \033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m
\033[3mINVESTER: AMPLIFIED\033[0m là bản làm lại của \033[3mINVESTER\033[0m. Đây là trò chơi miễn phí và mã nguồn mở.
CHỊU TRÁCH NGHIỆM SẢN XUẤT     ThienFakeVN
NỘI DUNG TRÒ CHƠI              ThienFakeVN
VIẾT MÃ                        ThienFakeVN

\033[1mGIẤY PHÉP\033[0m
Giấy phép được sử dụng: GNU General Public License v3.0

\033[1mSPECIAL THANKS\033[0m (khá xàm)
Ngân hàng Trung ương Liên Bang Nga (phát hành đồng rúp Nga, đồng tiền được sử dụng trong trò chơi là rúp Nga, nếu bạn chưa để ý)
w3schools.com (nơi đầu tiên tôi bắt đầu học lập trình)
Đứa nào đó tên là Thanh Bình học cùng trường với tôi (công ty \033[38;2;163;73;164mB\033[0m trong trò chơi là viết tắt của \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m mà, đúng không?)
Và vâng, không thể thiếu, chính là các bạn! (những người đã chơi trò chơi này)''')
    elif command.casefold() == 'aboutupdate': print('''
\033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m là bản cập nhật đầu tiên của \033[3mINVESTER: AMPLIFIED\033[0m.''')
    elif command.casefold() == 'update': update()
    else: print('Không hợp lệ, nhập "?" để xem danh sách các lệnh.')
    action()

def play(): 
    global money, game_seed, data_game, turns, A, B, C
    game_seed = input('Nhập một seed cho trò chơi (bỏ trống để có một seed ngẫu nhiên): ')
    if game_seed == '':
        game_seed = random.random()
        game_seed = int(game_seed // 0.00000000001)
    else:
        try: game_seed = int(game_seed)
        except ValueError: game_seed = hash(game_seed)
    random.seed(game_seed)
    data_game = {'game': 'invester', 'version': '1.0.0', 'seed': game_seed}
    money = 100
    turns = 1
    A, B, C = 100000000, 100000000, 100000000
    while turns >= 0:
        print()
        print(f'Lượt {turns}')
        while True:
            a, b, c = input('Chọn số tiền để mua cổ phần công ty \033[38;2;63;72;204mA\033[0m: '), input('Chọn số tiền để mua cổ phần công ty \033[38;2;163;73;164mB\033[0m: '), input('Chọn số tiền để mua cổ phần công ty \033[38;2;136;0;21mC\033[0m: ')
            if a.casefold() == 'end' or b.casefold() == 'end' or c.casefold() == 'end': game_over()
            try:
                a = int(a)
                b = int(b)
                c = int(c)
            except ValueError:
                print('Lỗi: Vui lòng nhập một số nguyên dương.')
                continue
            if a < 0 or b < 0 or c < 0:
                print('Lỗi: Không thể nhập số âm.')
                continue
            elif a > money or b > money or c > money or a + b > money or b + c > money or a + c > money or a + b + c > money:
                print('Lỗi: Vui lòng không nhập quá số tiền hiện có.')
                continue
            elif a > A or b > B or c > C:
                print('Lỗi: Không thể nhập số tiền nhiều hơn tổng cổ phần của công ty.')
                continue
            else:
                money -= (a + b + c)
                a /= A
                b /= B
                c /= C
                print(f'''Bạn đã sở hữu
    - {a * 100}% cổ phần của công ty \033[38;2;63;72;204mA\033[0m;
    - {b * 100}% cổ phần của công ty \033[38;2;163;73;164mB\033[0m;
    - {c * 100}% cổ phần của công ty \033[38;2;136;0;21mC\033[0m;
    - Còn {money} rúp.''')
                data_game.update({f'turn {turns}': {'owned A': a, 'owned B': b, 'owned C': c}})
                break
        print()
        A *= random.choice([0.8, 1, 2])
        B *= random.choice([0.1, 0.5, 1, 5, 10])
        C *= random.choice([0.01, 0.05, 0.01, 1, 100000])
        if A < 1000000: A = 1000000
        if B < 1000000: B = 1000000
        if C < 1000000: C = 1000000
        A, B, C = int(A), int(B), int(C)
        print(f'''Sau khi các công ty đầu tư, thực hiện dự án:
    - Tổng cổ phần của công ty \033[38;2;63;72;204mA\033[0m: {A} rúp;
    - Tổng cổ phần của công ty \033[38;2;163;73;164mB\033[0m: {B} rúp;
    - Tổng cổ phần của công ty \033[38;2;136;0;21mC\033[0m: {C} rúp.''')
        data_game[f'turn {turns}'].update({"A's equity": A, "B's equity": B, "C's equity": C})
        a *= A
        b *= B
        c *= C
        a, b, c = int(a), int(b), int(c)
        money += (a + b + c)
        print()
        print(f'''Bạn đã bán đống cồ phẩn:
    - Tiền nhận được từ công ty \033[38;2;63;72;204mA\033[0m: {a} rúp;
    - Tiền nhận được từ công ty \033[38;2;163;73;164mB\033[0m: {b} rúp;
    - Tiền nhận được từ công ty \033[38;2;136;0;21mC\033[0m: {c} rúp;''')
        data_game[f'turn {turns}'].update({'collected from A': a, 'collected from B': b, 'collected from C': c})
        if a + b + c > 2000000:
            if a + b + c > 5000000:
                if a + b + c > 10000000: tax = money * 0.5
                else: tax = money * 0.2
            else: tax = money * 0.1
        else: tax = money * 0
        tax = int(tax)
        money -= tax
        print(f'''
Thuế {tax} rúp!
''')
        print(f'''Tổng số tiền sau lượt {turns} là {money}.''')
        data_game[f'turn {turns}'].update({'tax': tax, 'money collected': money})
        if money <= 0: game_over()
        turns += 1

def money_input(): pass

def game_over():
    random.seed(None)
    print()
    print('Bạn hết tiền! Trò chơi kết thúc!')
    print(f'Trước khi đi, seed của trò chơi của bạn là {game_seed}.')
    command = input(f'Và bạn có thể lưu dữ liệu của trò chơi này vào một tệp .json bằng cách nhập "SAVE": ')
    while command.casefold() == 'save':
        location = input('Nhập vị trí lưu trò chơi: ')
        game_code = random.randint(1, 999999999999999999999999)
        try:
            with open(f'{location}\\invested{game_code}.json', 'w', encoding='utf-8') as invested:
                json.dump(data_game, invested, indent = 4)
        except PermissionError:
            print(f'Lỗi: Quyền bị từ chối: {location}\\invested{game_code}.json')
            continue
        except FileNotFoundError:
            print(f'Lỗi: Không có thư mục nào: {location}\\invested{game_code}.json')
            continue
        except:
            print('Một lỗi không xác định xuất hiện!')
            continue
        print(f'Đã xong! Vị trí của tệp: {location}\\invested{game_code}.json')
        break
    action()

def read():
    print()
    while True:
        saved_data_location = input('Nhập địa chỉ của tệp .json: ')
        try: 
            with open(saved_data_location, 'r', encoding='utf-8') as saved_data_file:
                saved_data = json.load(saved_data_file)
        except PermissionError:
            print(f'Lỗi: Quyền bị từ chối: {saved_data_location}')
            continue
        except FileNotFoundError:
            print(f'Lỗi: Không có thư mục nào: {saved_data_location}')
            continue
        try:
            if saved_data['game'] == 'invester':
                print(f'''
Phiên bản: {saved_data['version']}
Seed: {saved_data['seed']}''')
                turns = 1
                while turns:
                    print(f'''
Lượt {turns}:
    - Sở hữu cổ phần công ty \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']['owned A'] * 100}%;
    - Sở hữu cổ phần công ty \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']['owned B'] * 100}%;
    - Sở hữu cổ phần công ty \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']['owned C'] * 100}%;

    - Tổng cổ phần công ty \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']["A's equity"]} rúp;
    - Tổng cổ phần công ty \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']["B's equity"]} rúp;
    - Tổng cổ phần công ty \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']["C's equity"]} rúp;

    - Số tiền từ công ty \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']['collected from A']} rúp;
    - Số tiền từ công ty \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']['collected from B']} rúp;
    - Số tiền từ công ty \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']['collected from C']} rúp;

    - Thuế: {saved_data[f'turn {turns}']['tax']} rúp;

    - Tổng số tiền nhận được: {saved_data[f'turn {turns}']['money collected']} rúp.''')
                    turns += 1
                    if int(saved_data[f'turn {turns - 1}']['money collected']) < 0: action()
        except KeyError:
            print()
            print('Lỗi: Có vẻ như đây không phải là tệp có dữ liệu trò chơi này.')
            continue

def update():
    try: import requests
    except ModuleNotFoundError:
        print('Lỗi: Mô đun requests không được tìm thấy. Kiểm tra xem bạn đã cài đặt mô đun này chưa.')
        action()
    print()
    updates = requests.get('https://raw.githubusercontent.com/ThienFakeVN/invester/refs/heads/main/many_updates.py')
    environment = {}
    print('Các bản cập nhật có sẵn hiện tại:')
    exec(updates.content, environment)
    while True:
        chosen_update = input('Chọn bản cập nhật bạn muốn chơi: ')
        for update in environment['updates']:
            if update == chosen_update:
                print('Đã tìm thấy bản cập nhật.')
                command = input('Nhập "UPDATE" để cập nhật: ')
                if command.casefold() == 'update':
                    file_path = os.path.abspath(__file__)
                    update_content = requests.get(f'https://raw.githubusercontent.com/ThienFakeVN/invester/refs/heads/main/invester{chosen_update}.py')
                    with open(file_path, 'wb') as rewrite:
                        rewrite.write(update_content.content)
                        exit()
                else: action()
            else:
                print('Không tìm thấy bản cập nhật nào.')
                continue

print('''
(Gọi đây là khu vực action, nơi bạn sử dụng các lệnh)''')
action()
""")
    
elif language.casefold() == 'english': exec(r"""
import random, os, json

'''
EVEN THOUGH THIS GAME IS OPEN-SOURCE, DO NOT EDIT THE GAME'S CODE
IT MAY CAUSE UNEXPECTED ERRORS!
'''

print()
print('You have 100 Russian roubles. You are going to invest.')
print('Welcome to \033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m!')

def action():
    print()
    command = None
    command = input('Enter a command, such as "START" to start the game, "STORY" to view the story or "?" to see the list of commands: ')
    if command.casefold() == 'start': play()
    elif command.casefold() == 'story': print('''
There are 3 companies:
    - \033[38;2;63;72;204mA\033[0m company: Stands for \033[38;2;63;72;204;4mA\033[38;2;63;72;204mđù\033[0m (Vietnamese:~ Damn). Low profits and losses, less losses than profits;
    - \033[38;2;163;73;164mB\033[0m company: Stands for, uhh... \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m, I guess? Yep, \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m. "Trung bình" (Vietnamese: medium) profits and losses;
    - \033[38;2;136;0;21mC\033[0m company: Stands for \033[38;2;136;0;21;4mC\033[38;2;136;0;21moin \033[38;2;136;0;21;4mC\033[38;2;136;0;21mard\033[0m (based on a Vietnamese joke). Profits will make you rich, otherwise you are bankrupt. Less profits than losses, unfortunately. Perhaps they use your money to gamble.
You will buy equity of companies and sell them, changes of total equity of companies will affect your money and how much money will you gain/lose depends on how much equity you own.
(Và bạn không hề quan tâm đến việc điều hành công ty, nên mua bao nhiêu cổ phần thì bạn cũng không làm ảnh hưởng đến các quyết định của công ty)
(And you don't care about managing companies, so you won't influence companies' choices and actions no matter how much equity you have)
Also, if your income is too high the Democratic Socialist government will tax you, but you won't receive financial assistance if you run out of money because, simple, you don't make anything for society, you just sit there and (hope that you will) receive money.
(Speak about assistance, if a company is bankrupt, they will also get help)
The best of luck with your 100 Russian roubles!''')
    elif command.casefold() == 'help' or command.casefold() == '?' : print('''
ABOUTME/ABOUTUS     Displays information about me — creator of this game
ABOUTUPDATE         Displays information about the version
CREDITS             Displays information about the game's publisher
CWD                 Displays the current working directory
HELP/?              Displays the list of commands you can use at the action area
READ                Reads a .json file contains a game's data
START               Starts the game
STORY               Tells the story of the game
UPDATE              Finds and change the game's version (requires requests module)''')
    elif command.casefold() == 'cwd': print(f'''
Current working directory: {os.getcwd()}. This is where game's data files will be saved if you choose to save them.''')
    elif command.casefold() == 'read': read()
    elif command.casefold() == 'aboutme' or command.casefold() == 'aboutus': print('''
My name is Thiện, you can call me ThienFakeVN or ThieenjVN.
I am the only one who created this game. This game is also the first game I have ever created.
My games are free-to-play and open-source. They use the Terminal screen and are written in Python. Their content is both simple and complicated, based on what I am thinking about.
My GitHub account for anyone needs it: ThienFakeVN.''')
    elif command.casefold() == 'credits' or command.casefold() == 'credit': print('''
\033[1mCREDITS — \033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m
\033[3mINVESTER: AMPLIFIED\033[0m is the remake edition of \033[3mINVESTER\033[0m. This game is free-to-play and open-source.
PUBLISHER          ThienFakeVN
GAME'S CONTENT     ThienFakeVN
CODE WRITER        ThienFakeVN

\033[1mLICENCE\033[0m
Used licence: GNU General Public License v3.0

\033[1mSPECIAL THANKS\033[0m (kinda stupid)
Central Bank of the Russian Federation (issuing Russian rouble, if you don't know, it is used in this game)
w3schools.com (the first place I started learning programming)
A student named Thanh Bình who goes to the same school with me (\033[38;2;163;73;164mB\033[0m company stands for \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m, doesn't it?)
And of course, you (who are playing this game)''')
    elif command.casefold() == 'aboutupdate': print('''
\033[3mINVESTER: AMPLIFIED (v1.0.0)\033[0m is the first update of \033[3mINVESTER: AMPLIFIED\033[0m.''')
    elif command.casefold() == 'update': update()
    else: print('Invaild command, enter "?" to see the list of commands.')
    action()

def play(): 
    global money, game_seed, data_game, turns, A, B, C
    game_seed = input('Choose a seed (leave this empty to have a random seed): ')
    if game_seed == '':
        game_seed = random.random()
        game_seed = int(game_seed // 0.00000000001)
    else:
        try: game_seed = int(game_seed)
        except ValueError: game_seed = hash(game_seed)
    random.seed(game_seed)
    data_game = {'game': 'invester', 'version': '1.0.0', 'seed': game_seed}
    money = 100
    turns = 1
    A, B, C = 100000000, 100000000, 100000000
    while turns >= 0:
        print()
        print(f'Lượt {turns}')
        while True:
            a, b, c = input('Choose an amount of money to buy a portion of equity of \033[38;2;63;72;204mA\033[0m: '), input('Choose an amount of money to buy a portion of equity of \033[38;2;163;73;164mB\033[0m: '), input('Choose an amount of money to buy a portion of equity of \033[38;2;136;0;21mC\033[0m: ')
            if a.casefold() == 'end' or b.casefold() == 'end' or c.casefold() == 'end': game_over()
            try:
                a = int(a)
                b = int(b)
                c = int(c)
            except ValueError:
                print('Error: Please enter a positive integer.')
                continue
            if a < 0 or b < 0 or c < 0:
                print('Error: Cannot enter a negative number.')
                continue
            elif a > money or b > money or c > money or a + b > money or b + c > money or a + c > money or a + b + c > money:
                print('Error: The amount of money you chose cannot be more than the amount you have.')
                continue
            elif a > A or b > B or c > C:
                print('Error: The amount of money you chose cannot be more than the total equity of the company.')
                continue
            else:
                money -= (a + b + c)
                a /= A
                b /= B
                c /= C
                print(f'''You have owned
    - {a * 100}% equity of \033[38;2;63;72;204mA\033[0m;
    - {b * 100}% equity of \033[38;2;163;73;164mB\033[0m;
    - {c * 100}% equity of \033[38;2;136;0;21mC\033[0m;
    - {money} rouble(s) remained.''')
                data_game.update({f'turn {turns}': {'owned A': a, 'owned B': b, 'owned C': c}})
                break
        print()
        A *= random.choice([0.8, 1, 2])
        B *= random.choice([0.1, 0.5, 1, 5, 10])
        C *= random.choice([0.01, 0.05, 0.01, 1, 100000])
        if A < 1000000: A = 1000000
        if B < 1000000: B = 1000000
        if C < 1000000: C = 1000000
        A, B, C = int(A), int(B), int(C)
        print(f'''After changes:
    - Total equity of \033[38;2;63;72;204mA\033[0m: {A} roubles;
    - Total equity of \033[38;2;163;73;164mB\033[0m: {B} roubles;
    - Total equity of \033[38;2;136;0;21mC\033[0m: {C} roubles.''')
        data_game[f'turn {turns}'].update({"A's equity": A, "B's equity": B, "C's equity": C})
        a *= A
        b *= B
        c *= C
        a, b, c = int(a), int(b), int(c)
        money += (a + b + c)
        print()
        print(f'''You have sold the equity you owned:
    - Received money from \033[38;2;63;72;204mA\033[0m company: {a} roubles;
    - Received money from \033[38;2;163;73;164mB\033[0m company: {b} roubles;
    - Received money from \033[38;2;136;0;21mC\033[0m company: {c} roubles;''')
        data_game[f'turn {turns}'].update({'collected from A': a, 'collected from B': b, 'collected from C': c})
        if a + b + c > 2000000:
            if a + b + c > 5000000:
                if a + b + c > 10000000: tax = money * 0.5
                else: tax = money * 0.2
            else: tax = money * 0.1
        else: tax = money * 0
        tax = int(tax)
        money -= tax
        print(f'''
You pay {tax} roubles in tax!
''')
        print(f'''Total money after turn {turns}: {money}.''')
        data_game[f'turn {turns}'].update({'tax': tax, 'money collected': money})
        if money <= 0: game_over()
        turns += 1

def money_input(): pass

def game_over():
    random.seed(None)
    print('')
    print('You ran out of money! THe game is over!')
    print(f'Before you go, the seed of this game was {game_seed}.')
    command = input(f'''And you can save this game's data into a .json file by enter "SAVE": ''')
    while command.casefold() == 'save':
        location = input("Enter the file's location: ")
        game_code = random.randint(1, 999999999999999999999999)
        try:
            with open(f'{location}\\invested{game_code}.json', 'w', encoding='utf-8') as invested:
                json.dump(data_game, invested, indent = 4)
        except PermissionError:
            print(f'Error: Permission denied: {location}\\invested{game_code}.json')
            continue
        except FileNotFoundError:
            print(f'Error: No such directory: {location}\\invested{game_code}.json')
            continue
        print(f'Finished! File location: {location}\\invested{game_code}.json')
        break
    action()

def read():
    print('')
    while True:
        saved_data_location = input("Enter the .json file's location: ")
        try: 
            with open(saved_data_location, 'r', encoding='utf-8') as saved_data_file:
                saved_data = json.load(saved_data_file)
        except PermissionError:
            print(f'Error: Permission denied: {saved_data_location}')
            continue
        except FileNotFoundError:
            print(f'Error: No such directory: {saved_data_location}')
            continue
        try:
            if saved_data['game'] == 'invester':
                print(f'''
Version: {saved_data['version']}
Seed: {saved_data['seed']}''')
                turns = 1
                while turns:
                    print(f'''
Lượt {turns}:
    - Owned \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']['owned A'] * 100}%;
    - Owned \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']['owned B'] * 100}%;
    - Owned \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']['owned C'] * 100}%;

    - Total \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']["A's equity"]} roubles;
    - Total \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']["B's equity"]} roubles;
    - Total \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']["C's equity"]} roubles;

    - Collected from \033[38;2;63;72;204mA\033[0m: {saved_data[f'turn {turns}']['collected from A']} roubles;
    - Collected from \033[38;2;163;73;164mB\033[0m: {saved_data[f'turn {turns}']['collected from B']} roubles;
    - Collected from \033[38;2;136;0;21mC\033[0m: {saved_data[f'turn {turns}']['collected from C']} roubles;

    - Tax: {saved_data[f'turn {turns}']['tax']} roubles;

    - Total money collected: {saved_data[f'turn {turns}']['money collected']} roubles.''')
                    turns += 1
                    if int(saved_data[f'turn {turns - 1}']['money collected']) < 0: action()
        except KeyError:
            print()
            print("Error: Looks like this file doesn't contain this game's data.")
            continue

def update():
    try: import requests
    except ModuleNotFoundError:
        print('Error: Requests module not found. Please make sure that you have downloaded this module.')
        action()
    print('')
    updates = requests.get('https://raw.githubusercontent.com/ThienFakeVN/invester/refs/heads/main/many_updates.py')
    environment = {}
    print('Available update versions:')
    exec(updates.content, environment)
    while True:
        chosen_update = input('Choose the version you want to play: ')
        for update in environment['updates']:
            if update == chosen_update:
                print('The version was found!')
                command = input('Enter "UPDATE" to update: ')
                if command.casefold() == 'update':
                    file_path = os.path.abspath(__file__)
                    update_content = requests.get(f'https://raw.githubusercontent.com/ThienFakeVN/invester/refs/heads/main/invester{chosen_update}.py')
                    with open(file_path, 'wb') as rewrite:
                        rewrite.write(update_content.content)
                        exit()
                else: action()
            else:
                print('No version was found.')
                continue

print('''
(Call this place action area, where you can run commands)''')
action()
""")