models = ['NamaKantor', 'Kota', 'Alamat', 'NomorTelpon', 'Email', 'Longitude', 'Latitude' ]

cmd1 = '''
       <div class="form-group">
        <strong>_k:</strong>
        <InputText class="form-control" @bind-Value="@Model._k" />
       </div>'''
      
print ('----------------------------')
for m in models:
    print (cmd1.replace('_k', m))
    

models1 = ['Nama', 'NRP','Pangkat', 'NomorTelpon' ]
    
models_old = ['NomorLaporan', 'TanggalLaporan', 'UraianSingkat', 
          'FotoPath', 'Nama', 'NamaPanggilan', 'NIK', 'NKK',
          'NoPaspor', 'NoKitap', 'KodeSidikJari1', 'KodeSidikJari2',
          'JenisKelamin', 'LahirTempat', 'LahirTanggal',
          'Pendidikan', 'Pekerjaan', 'GolonganDarah',
          'StatusPerkawinan', 'Kewarganegaraan', 'NomorTelpon', 'Email',
          'KtpProvinsi', 'KtpKota', 'KtpKecamatan', 'KtpKelurahan', 'KtpAlamat',
          'DomProvinsi', 'DomKota', 'DomKecamatan', 'DomKelurahan', 'DomAlamat',
          'NamaAyah', 'NamaIbu', 'OrangtuaAlamat', 'OrangtuaTelpon', 'NamaAnak',
          
          'ModusOperandi', 'PasalYgDisangkakan', 'TKP', 
          'BarangJenis', 'BarangBerat', 'KendaraanDigunakan', 
          'KendaraanNomorPolisi', 'RekeningBankNomor', 'RekeningBankNama',
          'JaringanAtas', 'JaringanBawah', 'UraianKasusSebelumnya',
          'PenyidikNama', 'PenyidikNRP', 'PenyidikPangkat', 'PenyidikNomorTelpon']

