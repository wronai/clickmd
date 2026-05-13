## 2. Kolorowe statusy

✅ Zapisano plik
⚠️  Dysk prawie pełny
🛑 Brak połączenia
ℹ️  Przetwarzanie...

## 3. Kod z kolorowaniem


```python
print('Hello, World!')
```


```bash
curl -X GET https://api.example.com
```


```sql
SELECT * FROM users WHERE active = true;
```


## 4. Szybka tabela

```
┌───────────┬───────────┐
│Kolumna A  │Kolumna B  │
├───────────┼───────────┤
│Wartość 1  │Wartość 2  │
└───────────┴───────────┘
```

## 5. Panel informacyjny

```
┌── Uwaga ─────────────────────────────────────────────────────────────────┐
│ Ważna informacja!                                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

## 6. Progress bar

✅ Processing completed

## Porównanie: print() vs clickmd

| Zadanie | print() | clickmd |
|---------|---------|---------|
| Nagłówek | `print("# Title")` | `clickmd.md("# Title")` |
| Success | `print("\033[92m✅\033[0m")` | `clickmd.success("OK")` |
| Tabela | 20+ linii kodu | `clickmd.table(...)` |
| Progress | zewnętrzna lib | `clickmd.progress(...)` |

Wniosek: Ten sam efekt, mniej kodu, lepszy UX!

