<h2>Compiler Online</h2>

<textarea id="codeInput" rows="10" cols="50">
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
</textarea>
<br>
<button id="runButton">Run Code</button>
<pre id="output"></pre>

<script>
document.getElementById('runButton').addEventListener('click', async () => {
   console.log('click')
    const code = document.getElementById('codeInput').value;
    const response = await fetch('http://127.0.0.1:5000/compile', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
    });
    const result = await response.json();
    document.getElementById('output').innerText = result.output || result.error;
});
</script>

# Persiapan Lingkungan Pengembangan C++ 🛠️

Sebelum memulai perjalanan belajar C++, kita perlu menyiapkan beberapa tools dan lingkungan pengembangan. Panduan ini akan membantu Anda menyiapkan semua yang diperlukan untuk memulai coding.

## Compiler C++ 💻

### MinGW (Minimalist GNU for Windows)

MinGW adalah implementasi compiler GCC untuk Windows. Berikut langkah-langkah instalasinya:

1. **Download MinGW**
   - Kunjungi [MinGW Website](https://www.mingw-w64.org/)
   - Download installer yang sesuai dengan sistem operasi Anda
   - Pilih versi x86_64 untuk sistem 64-bit

2. **Instalasi MinGW**
   ```bash
   # Langkah instalasi:
   1. Jalankan installer
   2. Pilih arsitektur: x86_64
   3. Pilih threads: posix
   4. Pilih exception: seh
   ```

3. **Setup Path Environment**
   - Buka "System Properties" → "Advanced" → "Environment Variables"
   - Tambahkan path MinGW/bin ke System Path
   - Contoh path: `C:\MinGW\bin`

4. **Verifikasi Instalasi**
   ```bash
   g++ --version
   ```

## IDE/Text Editor 📝

### Visual Studio Code (Recommended)

VSCode adalah editor ringan namun powerful dengan dukungan C++ yang baik.

1. **Download dan Install**
   - Download [Visual Studio Code](https://code.visualstudio.com/)
   - Ikuti proses instalasi default

2. **Extensions yang Diperlukan**
   - C/C++ Extension Pack
   - Code Runner
   - Competitive Programming Helper (optional)

3. **Konfigurasi VSCode untuk C++**
   ```json
   // settings.json
   {
       "code-runner.runInTerminal": true,
       "code-runner.saveFileBeforeRun": true,
       "files.associations": {
           "*.cpp": "cpp"
       }
   }
   ```

### Alternatif IDE

1. **Dev-C++**
   - IDE ringan dan mudah digunakan
   - Cocok untuk pemula
   - [Download Dev-C++](https://www.bloodshed.net/)

2. **CodeBlocks**
   - Open source IDE
   - Cross-platform
   - [Download CodeBlocks](http://www.codeblocks.org/)

## Online Judges 🌐

Untuk competitive programming, daftar di platform berikut:

1. **Codeforces**
   - [Daftar di Codeforces](https://codeforces.com/)
   - Platform competitive programming terpopuler
   - Contest reguler
   - Rating system

2. **AtCoder**
   - [Daftar di AtCoder](https://atcoder.jp/)
   - Kontes berkualitas tinggi
   - Bagus untuk pemula

3. **SPOJ**
   - [Daftar di SPOJ](https://www.spoj.com/)
   - Koleksi soal klasik
   - Bagus untuk latihan

## Template Dasar C++ 📄

Gunakan template berikut untuk competitive programming:

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    // Kode solusi Anda di sini
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    // cin >> t;  // Uncomment untuk multiple test cases
    while(t--) {
        solve();
    }
    return 0;
}
```

## Verifikasi Setup ✅

Untuk memastikan semua sudah terpasang dengan benar:

1. **Buat File Test**
   ```cpp
   // test.cpp
   #include <iostream>
   using namespace std;
   
   int main() {
       cout << "Setup berhasil!" << endl;
       return 0;
   }
   ```

2. **Compile dan Jalankan**
   ```bash
   g++ test.cpp -o test
   ./test
   ```

## Tips Tambahan 💡

1. **Keyboard Shortcuts**
   - Pelajari shortcuts VSCode untuk coding lebih efisien
   - Gunakan snippets untuk kode yang sering digunakan

2. **Git untuk Version Control**
   - Install [Git](https://git-scm.com/)
   - Berguna untuk menyimpan progress belajar

3. **Competitive Companion**
   - Extension browser untuk parse soal contest
   - Support untuk berbagai online judges

## Troubleshooting 🔧

### Common Issues

1. **Compiler tidak ditemukan**
   ```bash
   # Solusi:
   - Periksa Path Environment
   - Restart VSCode/terminal
   ```

2. **Program tidak bisa dijalankan**
   ```bash
   # Periksa:
   - File permissions
   - Antivirus blocking
   - Nama file output
   ```

---

Setelah menyelesaikan setup ini, Anda siap untuk memulai perjalanan programming C++! 🚀

!!! tip "Pro Tip"
    Simpan semua kode latihan Anda dalam repository Git untuk tracking progress dan backup.