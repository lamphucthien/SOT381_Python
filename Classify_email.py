def classify_email(prob_spam):
    if prob_spam > 0.9:
        return "Spam"
    elif prob_spam > 0.5:
        return "Có thể là spam"
    else:
        return "Không phải spam"

while True:
    try:
        xac_suat = input("Hãy nhập xác suất, hoặc ấn f để kết thúc: ")
        if xac_suat.lower() == "f":
            print("Kết thúc")
            break

        prob = float(xac_suat)
        ket_qua = classify_email(prob)
        print("Kết quả phân loại:", ket_qua)
    except ValueError:
        print("Vui lòng nhập số hợp lệ, hoặc ấn f để kết thúc")