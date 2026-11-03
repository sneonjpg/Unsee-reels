# Canonical Unsee logo: geometry from Neo's brand-bible image (1080 sq): "uns" + clipped "e" under a lime bar with a peeled corner flap.
CREAM='#F2EFE6'
def logo(cx,cy,s=1.0,rot=0,tex=True):
    t=f'translate({cx} {cy}) rotate({rot}) scale({s}) translate(-528 -581)'
    texl='<rect x="636" y="501" width="316" height="188" filter="url(#tx)" opacity=".4"/>' if tex else ''
    return f'''<g transform="{t}"><text x="96" y="668" font-size="280" letter-spacing="-13" fill="{CREAM}" font-family="Inter,sans-serif" font-weight="900">unsee</text>
<g filter="url(#sh)"><rect x="636" y="501" width="316" height="188" fill="#C8F032"/>{texl}<rect x="636" y="501" width="316" height="188" fill="none" stroke="#e6ff7a" stroke-width="2" opacity=".3"/>
<path d="M591 473 L636 501 L643 553Z" fill="#9DBB1E"/><path d="M591 473 L643 553" stroke="#eaff8a" stroke-width="2" opacity=".6"/></g></g>'''
