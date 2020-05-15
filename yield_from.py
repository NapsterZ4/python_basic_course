def listar_cursos(*cursos):
    for elemento in cursos:
        yield from elemento


# Retorna los elementos hijos de la clase padre o principal
cursos_listado = listar_cursos("CTA", "Mat", "Fis", "lenguaje")
print(next(cursos_listado))