**PROJEKT SQL + PostgreSQL + Python + reálná data**:

* realistický (pracuje s daty obcí ČR),
* technicky zvládnutelný pro SŠ,
* dobře hodnotitelný,
* rozšiřitelný pro lepší studenty.

databáze obce:

* `okresy(id_okres, nazev)`
* `obce_pob(id_okres, id_obec, nazev, pocet_obyvatel, pocet_muzi, pocet_zeny, prumerny_vek, ...)`

---

# 🎯 Hlavní úkol (projekt):

## „Demografický přehled obcí ČR“

Vytvořte **konzolovou nebo jednoduchou GUI aplikaci v Pythonu**, která:

> umožní uživateli vyhledávat a analyzovat data o obyvatelstvu obcí a okresů.

---

# 🧩 Zadání

### Povinná část (základ – všichni musí splnit)

Aplikace musí:

### ✅ 1) Připojit se k PostgreSQL

* použít `psycopg`
* připojit se jako uživatel `student`
* databáze `obce`

---

### ✅ 2) Vypsat seznam okresů

Výstup:

```
CZ0100 Praha
CZ0201 Benešov
CZ0202 Beroun
...
```

(SQL: SELECT z tabulky `okresy`)

---

### ✅ 3) Zobrazit obce v okrese

Uživatel zadá kód okresu:

```
Zadej kód okresu: CZ0100
```

Výstup:

```
Praha — počet obcí: 1
Praha — obyvatel: 1 357 326
```

nebo:

```
Název obce | Obyvatel | Průměrný věk
```

(SQL JOIN)

---

### ✅ 4) Vyhledání obce podle názvu

Uživatel zadá část názvu:

```
Zadej název obce: nov
```

Výstup:

```
Nové Město na Moravě
Nová Paka
Nový Jičín
```

(SQL LIKE + parametrizovaný dotaz)

---

### ✅ 5) Statistika okresu

Program spočítá:

* celkový počet obyvatel
* průměrný věk
* poměr mužů/žen

Použít:

* `SUM()`
* `AVG()`
* `GROUP BY`

---

# 🧠 Co se máte naučit

| Oblast     | Co se studenti naučí             |
| ---------- | -------------------------------- |
| PostgreSQL | JOIN, agregace, GROUP BY         |
| Bezpečnost | parametrizované dotazy           |
| Python     | práce s DB, cykly, výpis tabulek |
| Praxe      | reálná databáze, ne umělá data   |

---

# 🖥 Doporučená struktura programu

```text
main.py
|
+-- connect()
+-- menu()
+-- vypis_okresu()
+-- obce_v_okrese()
+-- hledani_obce()
+-- statistika_okresu()
```

---

# 🧪 Ukázka menu vaší aplikace

```text
=========================
 DEMOGRAFIE ČR
=========================

1 - Seznam okresů
2 - Obce v okrese
3 - Hledat obec
4 - Statistiky okresu
0 - Konec

Vyber:
```

---

# 🟡 Bonus úkoly

### ⭐ Bonus 1 — Export do CSV

Uživatel:

```
Exportuj okres CZ0100 do CSV
```

Program:

* uloží soubor `praha.csv`
* zapíše data z databáze

---

### ⭐ Bonus 2 — Top 10 obcí

```text
TOP 10 největších obcí v ČR
```

SQL:

```
ORDER BY pocet_obyvatel DESC
LIMIT 10
```

---

### ⭐ Bonus 3 — Graf (matplotlib)

* sloupcový graf obyvatel v okrese
* porovnání mužů vs žen
