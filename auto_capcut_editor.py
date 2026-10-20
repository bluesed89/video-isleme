"""
Otomatik CapCut Kurgu ve Timeline Enjeksiyon Scripti (2-Saniye Hiper-Dinamik Motoru)
Kullanım:
    python auto_capcut_editor.py --plan "work_cca/edit_plan.json" --project-name "video1_coca_cola"
"""
import argparse
import os
import sys
import subprocess
import shutil
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "capcut-editing-automation", "capcut-editing-automation", "scripts")
CAPCUT_DRAFTS_DIR = os.path.expandvars(r"%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft")

def is_capcut_running():
    try:
        out = subprocess.check_output('tasklist /FI "IMAGENAME eq CapCut.exe"', shell=True).decode('utf-8', errors='ignore')
        return "CapCut.exe" in out
    except Exception:
        return False

def find_capcut_project(project_name):
    target = os.path.join(CAPCUT_DRAFTS_DIR, project_name)
    if os.path.isdir(target):
        return target
    # Search by draft_name in draft_meta_info.json
    if os.path.isdir(CAPCUT_DRAFTS_DIR):
        for entry in os.listdir(CAPCUT_DRAFTS_DIR):
            folder = os.path.join(CAPCUT_DRAFTS_DIR, entry)
            meta = os.path.join(folder, "draft_meta_info.json")
            if os.path.isfile(meta):
                try:
                    with open(meta, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if data.get("draft_name") == project_name:
                            return folder
                except Exception:
                    pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Otomatik CapCut Kurgu ve Timeline Enjeksiyon Motoru")
    parser.add_argument("--plan", required=True, help="edit_plan.json dosyasının yolu")
    parser.add_argument("--project-name", required=True, help="CapCut projesinin adı (Örn: video1_coca_cola)")
    parser.add_argument("--force", action="store_true", help="CapCut açık olsa bile zorla")
    args = parser.parse_args()

    print("=" * 65)
    print("🎬 2-SANİYE HİPER-DİNAMİK CAPCUT OTOMASYON MOTORU")
    print("=" * 65)

    if not args.force and is_capcut_running():
        print("❌ HATA: CapCut şu anda çalışıyor!")
        print("   Lütfen CapCut'ı tamamen kapatıp tekrar deneyin (Save & Quit).")
        print("   CapCut açıkken dosyalara yazılırsa CapCut kapanırken kurguyu ezer.")
        sys.exit(1)

    project_dir = find_capcut_project(args.project_name)
    if not project_dir:
        print(f"❌ HATA: CapCut proje klasörü bulunamadı: '{args.project_name}'")
        print(f"   Aranan dizin: {CAPCUT_DRAFTS_DIR}")
        sys.exit(1)
    print(f"📁 Proje Bulundu: {project_dir}")

    work_dir = os.path.dirname(os.path.abspath(args.plan))
    staging_proj = os.path.join(work_dir, "capcut_project")
    build_dir = os.path.join(work_dir, "build")
    os.makedirs(staging_proj, exist_ok=True)
    os.makedirs(build_dir, exist_ok=True)

    # 1. Proje meta ve içerik dosyalarını staging'e kopyala
    print("\n[1/3] Proje taslak dosyaları taranıyor ve kopyalanıyor...")
    for fn in ["draft_content.json", "draft_info.json", "draft_meta_info.json"]:
        src = os.path.join(project_dir, fn)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(staging_proj, fn))

    pj_dir = os.path.join(project_dir, "Timelines")
    if os.path.isdir(pj_dir):
        dst_pj = os.path.join(staging_proj, "Timelines")
        os.makedirs(dst_pj, exist_ok=True)
        pj_file = os.path.join(pj_dir, "project.json")
        if os.path.isfile(pj_file):
            shutil.copy2(pj_file, os.path.join(dst_pj, "project.json"))

    # 2. build_capcut.py çalıştır
    print("\n[2/3] Hiper-Dinamik 2-Saniye Kurgu Timeline'ı inşa ediliyor...")
    build_script = os.path.join(SCRIPTS_DIR, "build_capcut.py")
    cmd_build = [
        sys.executable,
        build_script,
        "--plan", os.path.abspath(args.plan),
        "--project", staging_proj,
        "--out", build_dir
    ]
    res_build = subprocess.run(cmd_build, cwd=SCRIPTS_DIR, capture_output=True, text=True)
    if res_build.returncode != 0:
        print("❌ Kurgu inşasında hata oluştu:")
        print(res_build.stdout)
        print(res_build.stderr)
        sys.exit(1)
    print(res_build.stdout.strip())

    # 3. install_to_project.py çalıştır
    print("\n[3/3] Bitmiş dinamik timeline CapCut projesine enjekte ediliyor...")
    install_script = os.path.join(SCRIPTS_DIR, "install_to_project.py")
    cmd_install = [
        sys.executable,
        install_script,
        "--build", build_dir,
        "--project", project_dir
    ]
    res_install = subprocess.run(cmd_install, cwd=SCRIPTS_DIR, capture_output=True, text=True)
    if res_install.returncode != 0:
        print("❌ Kurulumda hata oluştu:")
        print(res_install.stdout)
        print(res_install.stderr)
        sys.exit(1)
    print(res_install.stdout.strip())

    print("\n" + "=" * 65)
    print("✅ TEBRİKLER! HİPER-DİNAMİK KURGU BAŞARIYLA TAMAMLANDI!")
    print(f"🎬 CapCut'ı açıp '{args.project_name}' projesine girebilirsiniz.")
    print("   Tüm 2-saniye beat kesmeleri, karaktere zoomlar (%130),")
    print("   sağ-sol kamera geçişleri, pop-in altyazılar ve SFX'ler hazır!")
    print("=" * 65)

if __name__ == "__main__":
    main()
