models = ['NamaKantor', 'Kota', 'Alamat', 'NomorTelpon', 'Email', 'Longitude', 'Latitude' ]

cmd1 = '''
        <dt class="col-sm-3 bkanan">_k :</dt>
        <dd class="col-sm-9">@Model._k</dd>'''
      
print ('----------------------------')
for m in models:
    print (cmd1.replace('_k', m))
    

models_tersangka = ['NomorLaporan', 'TanggalLaporan', 'UraianSingkat', 
          'FotoPath', 'Nama', 'NamaPanggilan', 'NIK', 'NKK',
          'NoPaspor', 'NoKitap', 'KodeSidikJari1', 'KodeSidikJari2',
          'JenisKelamin', 'LahirTempat', 'LahirTanggal',
          'Pendidikan', 'Pekerjaan', 'GolonganDarah',
          'StatusPerkawinan', 'Kewarganegaraan', 'NomorTelpon', 'Email',
          'KtpProvinsi', 'KtpKota', 'KtpKecamatan', 'KtpKelurahan', 'KtpAlamat',
          'DomProvinsi', 'DomKota', 'DomKecamatan', 'DomKelurahan', 'DomAlamat',
          'NamaAyah', 'NamaIbu', 'OrangtuaAlamat', 'OrangtuaTelpon', 'NamaAnak']


models_penyidik = ['Nama', 'NRP','Pangkat', 'NomorTelpon' ]    
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
