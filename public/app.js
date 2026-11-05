/* RedAgro La Rioja — demo red social productiva */

const IMG = {
  aceituna: "assets/img/aceituna.jpg",
  aceite: "assets/img/aceite.jpg",
  nuez: "assets/img/nuez.jpg",
  nuezPelada: "assets/img/nuez-pelada.jpg",
  cereal: "assets/img/cereal.jpg",
  hortaliza: "assets/img/hortaliza.jpg",
  campo: "assets/img/olivar.jpg",
  saucesCover: "assets/img/campo-sauces.jpg",
  arauco: "assets/img/campo-arauco.jpg",
  llanos: "assets/img/campo-llanos.jpg",
};

const producers = {
  sauces: {
    title: "Finca Los Sauces · Chilecito",
    name: "José Vargas",
    meta: "Olivo · Nogal · Aceite",
    avatar: IMG.campo,
    ha: "12 ha",
    vol: "18 t",
    sale: "Mayorista",
    post: "Nueva partida de aceite lista para retiro en Chilecito. Consultas por mensaje privado.",
    products: [
      { title: "Aceituna Arauco", desc: "8 t · cosecha 2026", img: IMG.aceituna },
      { title: "Aceite EVO", desc: "Stock semanal · minorista", img: IMG.aceite },
      { title: "Nuez Chandler", desc: "4 t · packaging", img: IMG.nuez },
    ],
  },
  arauco: {
    title: "Establecimiento Norte · Arauco",
    name: "Ana Roldán",
    meta: "Nogal · Agrícola",
    avatar: IMG.arauco,
    ha: "28 ha",
    vol: "22 t",
    sale: "Mayorista",
    post: "Nogales en producción. Entrega a granel o con packaging.",
    products: [
      { title: "Nuez Chandler", desc: "12 t · packaging", img: IMG.nuez },
      { title: "Nuez pelada", desc: "Mayorista", img: IMG.nuezPelada },
    ],
  },
  llanura: {
    title: "Acopio Los Llanos · Chamical",
    name: "Cooperativa Sur",
    meta: "Acopio · Empaque",
    avatar: IMG.llanos,
    ha: "Planta",
    vol: "Variable",
    sale: "Mayorista",
    post: "Centro de acopio con empaque para el sur provincial.",
    products: [
      { title: "Cereales a granel", desc: "Retiro en planta", img: IMG.cereal },
      { title: "Hortalizas de estación", desc: "Minorista / mayorista", img: IMG.hortaliza },
    ],
  },
};

const pins = [
  {
    key: "sauces",
    title: "Finca Los Sauces",
    meta: "Chilecito · 12 ha · Acceso por RP 14",
    dist: "14 km",
    post: "Galpón + secadero",
    status: "Validado",
    products: [IMG.aceituna, IMG.aceite],
    lat: -29.1642,
    lng: -67.4975,
  },
  {
    key: "arauco",
    title: "Establecimiento Norte",
    meta: "Arauco · 28 ha · Acceso por RN 38",
    dist: "6 km",
    post: "Cámara de frío",
    status: "Validado",
    products: [IMG.nuez, IMG.nuezPelada],
    lat: -28.58,
    lng: -66.81,
  },
  {
    key: "llanura",
    title: "Acopio Los Llanos",
    meta: "Chamical · logística · Acceso rural",
    dist: "22 km",
    post: "Acopio + empaque",
    status: "Validado",
    products: [IMG.cereal, IMG.hortaliza],
    lat: -30.36,
    lng: -66.31,
  },
  {
    key: "sauces",
    title: "Capital · exhibición",
    meta: "La Rioja Capital · punto de referencia",
    dist: "—",
    post: "Vitrina urbana",
    status: "Referencia",
    products: [IMG.aceite, IMG.hortaliza],
    lat: -29.4131,
    lng: -66.8563,
  },
];

const rows = [
  { nombre: "Cooperativa Valle Verde", dept: "Chilecito", rubro: "Agrícola", fecha: "03/11/2026", estado: "Pendiente" },
  { nombre: "Estancia El Bermejo", dept: "Arauco", rubro: "Ganadero", fecha: "02/11/2026", estado: "Pendiente" },
  { nombre: "Huerta San Martín", dept: "Capital", rubro: "Agrícola", fecha: "01/11/2026", estado: "Observado" },
  { nombre: "Taller Textaña Riojana", dept: "Chamical", rubro: "Artesanal", fecha: "31/10/2026", estado: "Pendiente" },
  { nombre: "Finca Los Sauces", dept: "Chilecito", rubro: "Agrícola", fecha: "28/10/2026", estado: "Aprobado" },
];

const history = [
  "04/11/2026 — Lic. Pérez aprobó Finca Los Sauces (Chilecito).",
  "03/11/2026 — Tec. Ruiz observó Huerta San Martín: falta documentación de hectáreas.",
  "01/11/2026 — Lic. Pérez rechazó solicitud duplicada en Capital.",
];

let provinceMap;
let farmMap;
let selectedPin = 0;
const markers = [];

function argenmapLayer() {
  return L.tileLayer(
    "https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png",
    {
      attribution: "Argenmap © IGN Argentina",
      maxZoom: 18,
    }
  );
}

function osmLayer() {
  return L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap",
    maxZoom: 19,
  });
}

function pinIcon(celeste) {
  return L.divIcon({
    className: "pin-icon",
    html: `<div class="pin-bubble ${celeste ? "celeste" : ""}"></div>`,
    iconSize: [28, 28],
    iconAnchor: [14, 28],
    popupAnchor: [0, -24],
  });
}

function toggleMenu() {
  const topbar = document.getElementById("topbar");
  const toggle = document.getElementById("menuToggle");
  const backdrop = document.getElementById("navBackdrop");
  const open = !topbar.classList.contains("menu-open");
  topbar.classList.toggle("menu-open", open);
  toggle.setAttribute("aria-expanded", open ? "true" : "false");
  toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  if (backdrop) backdrop.hidden = !open;
}

function closeMenu() {
  const topbar = document.getElementById("topbar");
  const toggle = document.getElementById("menuToggle");
  const backdrop = document.getElementById("navBackdrop");
  if (!topbar) return;
  topbar.classList.remove("menu-open");
  if (toggle) {
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Abrir menú");
  }
  if (backdrop) backdrop.hidden = true;
}

function show(id) {
  document.querySelectorAll(".view").forEach((v) => v.classList.remove("active"));
  const view = document.getElementById(id);
  view.classList.add("active");
  document.querySelectorAll(".nav-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.route === id);
  });
  view.querySelectorAll(".reveal").forEach((el) => {
    el.style.animation = "none";
    void el.offsetWidth;
    el.style.animation = "";
  });
  closeMenu();
  window.scrollTo({ top: 0, behavior: "smooth" });
  requestAnimationFrame(() => {
    if (id === "mapa") ensureProvinceMap();
    if (id === "perfil") ensureFarmMap();
  });
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(toast._t);
  toast._t = setTimeout(() => el.classList.remove("show"), 2200);
}

function fillProducer(key) {
  const p = producers[key] || producers.sauces;
  document.getElementById("profileTitle").textContent = p.title;
  document.getElementById("profileName").textContent = p.name;
  document.getElementById("profileMeta").textContent = p.meta;
  document.getElementById("profileAvatar").src = p.avatar;
  document.getElementById("mHa").textContent = p.ha;
  document.getElementById("mVol").textContent = p.vol;
  document.getElementById("mSale").textContent = p.sale;
  document.getElementById("profilePost").textContent = p.post;
  document.getElementById("profileProducts").innerHTML = p.products
    .map(
      (item) => `
      <article class="produce">
        <img src="${item.img}" alt="${item.title}" />
        <h4>${item.title}</h4>
        <p>${item.desc}</p>
      </article>`
    )
    .join("");
}

function openProducer(key) {
  fillProducer(key);
  show("perfil");
}

function renderDiscover() {
  const list = document.getElementById("discoverList");
  const items = [
    { key: "sauces", title: "Finca Los Sauces", meta: "Chilecito · olivo", img: IMG.campo },
    { key: "arauco", title: "Establecimiento Norte", meta: "Arauco · nogal", img: IMG.arauco },
    { key: "llanura", title: "Acopio Los Llanos", meta: "Chamical · acopio", img: IMG.llanos },
  ];
  list.innerHTML = items
    .map(
      (i) => `
    <button type="button" class="discover-item" onclick="openProducer('${i.key}')">
      <img src="${i.img}" alt="${i.title}" />
      <div>
        <strong>${i.title}</strong>
        <span>${i.meta}</span>
      </div>
    </button>`
    )
    .join("");
}

function ensureProvinceMap() {
  const el = document.getElementById("provinceMap");
  if (!el || typeof L === "undefined") return;

  if (!provinceMap) {
    provinceMap = L.map(el, { scrollWheelZoom: true }).setView([-29.6, -66.95], 7);
    const argen = argenmapLayer();
    const osm = osmLayer();
    argen.addTo(provinceMap);
    L.control.layers({ Argenmap: argen, OpenStreetMap: osm }).addTo(provinceMap);

    pins.forEach((pin, index) => {
      const marker = L.marker([pin.lat, pin.lng], { icon: pinIcon(index % 2 === 1) }).addTo(provinceMap);
      marker.bindPopup(`<strong>${pin.title}</strong><br/>${pin.meta}`);
      marker.on("click", () => selectPin(index, false));
      markers.push(marker);
    });

    selectPin(0, false);
  }

  setTimeout(() => provinceMap.invalidateSize(), 120);
}

function ensureFarmMap() {
  const el = document.getElementById("farmMap");
  if (!el || typeof L === "undefined") return;

  if (!farmMap) {
    farmMap = L.map(el, { scrollWheelZoom: false }).setView([-29.1642, -67.4975], 14);
    argenmapLayer().addTo(farmMap);
    osmLayer(); // available if argenmap fails visually user can still have province switch

    const lots = [
      {
        name: "Lote A · Olivo",
        coords: [
          [-29.1618, -67.5012],
          [-29.1618, -67.4958],
          [-29.1655, -67.4958],
          [-29.1655, -67.5012],
        ],
        color: "#3a8fc4",
      },
      {
        name: "Lote B · Nogal",
        coords: [
          [-29.1658, -67.5010],
          [-29.1658, -67.4962],
          [-29.1692, -67.4962],
          [-29.1692, -67.5010],
        ],
        color: "#a51d24",
      },
    ];

    lots.forEach((lot) => {
      L.polygon(lot.coords, {
        color: lot.color,
        weight: 2,
        fillColor: lot.color,
        fillOpacity: 0.25,
      })
        .addTo(farmMap)
        .bindPopup(`<strong>${lot.name}</strong><br/>Finca Los Sauces`);
    });

    L.marker([-29.1642, -67.4975], { icon: pinIcon(false) })
      .addTo(farmMap)
      .bindPopup("<strong>Casco / galpón</strong><br/>Chilecito, La Rioja");
  }

  setTimeout(() => farmMap.invalidateSize(), 120);
}

function selectPin(index, fly = true) {
  selectedPin = index;
  const pin = pins[index];
  document.getElementById("pinTitle").textContent = pin.title;
  document.getElementById("pinMeta").textContent = pin.meta;
  document.getElementById("pinDist").textContent = pin.dist;
  document.getElementById("pinPost").textContent = pin.post;
  document.getElementById("pinStatus").textContent = pin.status;
  document.getElementById("pinProducts").innerHTML = pin.products
    .map((src) => `<img src="${src}" alt="Producto" />`)
    .join("");
  document.getElementById("pinOpenBtn").onclick = () => openProducer(pin.key);
  if (fly && provinceMap) {
    provinceMap.flyTo([pin.lat, pin.lng], 11, { duration: 0.9 });
  }
}

function flyToSelected() {
  if (!provinceMap) ensureProvinceMap();
  const pin = pins[selectedPin];
  provinceMap.flyTo([pin.lat, pin.lng], 12, { duration: 0.9 });
  markers[selectedPin]?.openPopup();
}

function adminTab(id) {
  document.querySelectorAll(".admin-tab").forEach((b) => {
    b.classList.toggle("active", b.dataset.admin === id);
  });
  document.querySelectorAll(".admin-panel").forEach((p) => {
    p.classList.toggle("active", p.id === `admin-${id}`);
  });
}

function renderTable() {
  const body = document.getElementById("acredBody");
  if (!body) return;
  const dept = document.getElementById("deptFilter").value;
  const rubro = document.getElementById("rubroFilter").value;
  body.innerHTML = "";
  rows
    .filter((r) => (dept === "all" || r.dept === dept) && (rubro === "all" || r.rubro === rubro))
    .forEach((r) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${r.nombre}</td>
        <td>${r.dept}</td>
        <td>${r.rubro}</td>
        <td>${r.fecha}</td>
        <td><span class="status ${r.estado === "Aprobado" ? "ok" : ""}">${r.estado}</span></td>
        <td class="row-actions">
          <button type="button" class="btn small ok" onclick="decide('${r.nombre.replace(/'/g, "\\'")}', 'aprobó')">Aprobar</button>
          <button type="button" class="btn small ghost" onclick="decide('${r.nombre.replace(/'/g, "\\'")}', 'observó')">Observar</button>
          <button type="button" class="btn small danger" onclick="decide('${r.nombre.replace(/'/g, "\\'")}', 'rechazó')">Rechazar</button>
        </td>`;
      body.appendChild(tr);
    });
}

function filterRows() {
  renderTable();
}

function decide(nombre, accion) {
  const stamp = new Date().toLocaleDateString("es-AR");
  history.unshift(`${stamp} — Agente ministerial ${accion} ${nombre}.`);
  renderHistory();
  toast(`Decisión registrada: ${accion} ${nombre}`);
}

function renderHistory() {
  const list = document.getElementById("historyList");
  if (!list) return;
  list.innerHTML = history
    .slice(0, 8)
    .map((h) => {
      const [date, ...rest] = h.split(" — ");
      return `<li><strong>${date}</strong><span>${rest.join(" — ")}</span></li>`;
    })
    .join("");
}

function renderModeration() {
  const list = document.getElementById("modList");
  if (!list) return;
  const items = [
    {
      title: "Comentario reportado · Finca Los Sauces",
      detail: "Lenguaje inadecuado en publicación de aceite EVO.",
    },
    {
      title: "Publicación observada · Acopio Los Llanos",
      detail: "Foto sin relación con el producto declarado.",
    },
    {
      title: "Mensaje bloqueado · Establecimiento Norte",
      detail: "Remitente reiterado sin identificación válida.",
    },
  ];
  list.innerHTML = items
    .map(
      (i) => `
    <div class="mod-item">
      <div>
        <strong>${i.title}</strong>
        <p>${i.detail}</p>
      </div>
      <div class="row-actions">
        <button type="button" class="btn small ghost" onclick="toast('Contenido ocultado')">Ocultar</button>
        <button type="button" class="btn small danger" onclick="toast('Remitente bloqueado')">Bloquear</button>
      </div>
    </div>`
    )
    .join("");
}

function renderFiscal() {
  const body = document.getElementById("fiscalBody");
  if (!body) return;
  const items = [
    ["Finca Los Sauces", "Chilecito", "12/10/2026", "OK", "Validado"],
    ["Establecimiento Norte", "Arauco", "08/10/2026", "OK", "Validado"],
    ["Acopio Los Llanos", "Chamical", "02/10/2026", "Pendiente", "En revisión"],
    ["Huerta San Martín", "Capital", "—", "Sin pin", "Observado"],
  ];
  body.innerHTML = items
    .map(
      (r) => `
    <tr>
      <td>${r[0]}</td>
      <td>${r[1]}</td>
      <td>${r[2]}</td>
      <td>${r[3]}</td>
      <td><span class="status ${r[4] === "Validado" ? "ok" : ""}">${r[4]}</span></td>
    </tr>`
    )
    .join("");
}

function generateFicha() {
  const input = document.getElementById("aiCrop").value.trim();
  const out = document.getElementById("aiOut");
  out.textContent = "Generando borrador…";
  setTimeout(() => {
    out.textContent =
      `Finca especializada en ${input || "producción local"}.\n\n` +
      "Producción riojana con trazabilidad digital: trabajos culturales, insumos declarados y geolocalización del establecimiento. " +
      "Comercialización mayorista, retiro en origen y vínculo logístico hacia rutas troncales.\n\n" +
      "Compromiso con BPA y transparencia para compradores.\n\n" +
      "— Borrador editable (demo).";
    toast("Borrador de ficha generado");
  }, 450);
}

renderDiscover();
renderTable();
renderHistory();
renderModeration();
renderFiscal();
fillProducer("sauces");
show("home");
