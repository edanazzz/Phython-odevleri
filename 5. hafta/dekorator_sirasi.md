# Görev 2: Dekoratör Sırası ve Çağrı Sayıları (fib(20))

Fibonacci(20) işlemi için ölçülen çağrı sayıları ve nedenleri aşağıdadır:

### 1. Yalnızca `@say` (21891 çağrı)
Fonksiyon daha önce hesapladığı hiçbir sonucu hatırlamaz (önbellek yoktur). Bu yüzden aynı sayıları defalarca baştan hesaplar ve sayaç her adımda artarak 21.891'e ulaşır.

### 2. `@say` üstte, `@lru_cache` altta (39 çağrı)
Dış kılıfta sayaç, iç kılıfta önbellek (hafıza) vardır. Python bir sayıyı hesaplamak istediğinde önce dışarıdaki sayaca çarpar (sayaç artar), sonra içeri girip önbelleğe bakar. Sonuç hafızada varsa bile sayaca çoktan temas edildiği için önbellekten dönen her deneme sayılmış olur. 

### 3. `@lru_cache` üstte, `@say` altta (21 çağrı)
Dış kılıfta önbellek, iç kılıfta sayaç vardır. Python çalışmaya başladığında ilk olarak dışarıdaki önbelleğe bakar. Eğer sonuç hafızadaysa, içeriye (sayaca) hiç girmeden sonucu direkt verir. Sayaç yalnızca daha önce hiç hesaplanmamış, yepyeni bir sayı geldiğinde artar. Bu yüzden en düşük çağrı sayısı elde edilir.
*(Not: Bu durumda sayaca dış kılıfı aşıp ulaşmak için `fib.__wrapped__.cagri` kullanılmıştır.)*
