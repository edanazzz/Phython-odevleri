def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Sahip olunan esyalara gore envanter metnini dondurur."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("guclu motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Verilen hedef gezegen listesini numaralandirarak menu metni olarak dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")

    return "\n".join(satirlar)
