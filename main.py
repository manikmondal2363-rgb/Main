import time
import sys
import os
from datetime import datetime, timedelta, timezone

# 🎨 Vibrant Color Palette
R, G, Y, B, P, C, W, X = "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m", "\033[1;37m", "\033[0m"

def start_universal_supreme():
    os.system('clear')
    print(f"{R}=========================================")
    print(f"{P}      UNIVERSAL SUPREME LIFE ENGINE      ")
    print(f"{C}      MASTERMIND: MANIK MONDAL           ")
    print(f"{R}========================================={X}")
    
    try:
        # ইনপুট সিস্টেম
        name = input(f"{Y}ENTER NAME: {X}").upper()
        dob = input(f"{Y}BIRTH DATE (YYYY,MM,DD): {X}")
        y_in, m_in, d_in = map(int, dob.split(','))
        
        birth_date = datetime(y_in, m_in, d_in, tzinfo=timezone.utc)
        birth_day_name = birth_date.strftime("%A").upper()
        
        print(f"\n{G}[SYSTEM]: GENERATING 16-LINE DASHBOARD...{X}\n")
        time.sleep(1)
        os.system('clear')

        while True:
            # বর্তমান সময় (IST)
            now_ist = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
            
            # --- দিন শেষ হওয়ার কাউন্টডাউন হিসাব ---
            # আজকের দিনের শেষ সময় (রাত ১১:৫৯:৫৯)
            tomorrow = datetime(now_ist.year, now_ist.month, now_ist.day) + timedelta(days=1)
            time_left = tomorrow - datetime(now_ist.year, now_ist.month, now_ist.day, now_ist.hour, now_ist.minute, now_ist.second)
            
            cd_h, rem = divmod(time_left.seconds, 3600)
            cd_m, cd_s = divmod(rem, 60)
            # --------------------------------------

            diff = now_ist - birth_date
            total_sec = int(diff.total_seconds())
            years = diff.days // 365
            months = (diff.days % 365) // 30
            weeks = (diff.days % 30) // 7
            rem_days = (diff.days % 30) % 7
            
            # ১৬ লাইনের স্থির আপডেট
            sys.stdout.write("\033[H") 
            
            print(f"{R}--- {P}{name}'S SUPREME STATUS {R}---{X}           ")
            print(f"{Y}TODAY'S DATE   : {W}{now_ist.strftime('%Y-%m-%d')}{X}               ")
            print(f"{G}TODAY'S DAY    : {W}{now_ist.strftime('%A').upper()}{X}               ")
            print(f"{R}-----------------------------------------{X}")
            print(f"{Y}BIRTH DATE     : {W}{y_in}-{m_in:02}-{d_in:02}{X}          ")
            print(f"{G}BIRTH DAY NAME : {W}{birth_day_name}{X}           ")
            print(f"{B}EXACT AGE      : {W}{years}Y {months}M {weeks}W {rem_days}D{X}  ")
            print(f"{C}TOTAL JOURNEY  : {W}{diff.days:,} DAYS{X}             ")
            print(f"{P}TOTAL HOURS    : {W}{total_sec // 3600:,} HOURS{X}            ")
            print(f"{Y}TOTAL SECONDS  : {W}{total_sec:,} SECS{X}             ")
            print(f"{B}LIFE PROGRESS  : {W}{(diff.days/(100*365))*100:.6f}%{X}      ")
            print(f"{R}-----------------------------------------{X}")
            print(f"{W}CURRENT TIME   : {G}{now_ist.strftime('%H:%M:%S')}{X}              ")
            # নতুন কাউন্টডাউন লাইন
            print(f"{P}DAY COUNTDOWN  : {R}-{cd_h:02}h {cd_m:02}m {cd_s:02}s{X} [LEFT]     ")
            print(f"{R}-----------------------------------------{X}")
            print(f"{C}      DESIGNED BY: MANIK MONDAL          {X}")
            
            sys.stdout.flush()
            time.sleep(1)
            
    except Exception as e:
        print(f"\n{R}ERROR: {e}{X}")

if __name__ == "__main__":
    start_universal_supreme()
