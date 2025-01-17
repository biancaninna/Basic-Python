nama_depan= "Bianca"
nama_tengah = "Ninna"
nama_belakang ="Sastro"

#kalo manualnya untuk menyapa nama lengkap seperti berikut
# sapa = 'Halo  '+ nama_depan+" "+nama_tengah+" "+nama_belakang
# print(sapa)

#kalo gini kan lumayan lama apalagi penambahannya banyak, makanya di python ada sebuah fitur disebut
#format string seperti dibawah ini :
sapa = f"Halo {nama_depan} {nama_tengah} {nama_belakang}"
print(sapa)

#harus ada f nya untuk memberi tau python bahwa ini adalah operasi string format dan kurungnya bukan 
#seperti kurung biasa() tapi kurung kurawa {}