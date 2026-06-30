import tkinter as tk
from tkinter import ttk
import math
import json
import os
import numpy as np

def Rx(a):
    return np.array([
        [1,0,0],
        [0,np.cos(a),-np.sin(a)],
        [0,np.sin(a), np.cos(a)]
    ])

def Ry(a):
    return np.array([
        [np.cos(a),0,np.sin(a)],
        [0,1,0],
        [-np.sin(a),0,np.cos(a)]
    ])

def wrap_180(x):
    return (x + 180) % 360 - 180

# --------------------------------------------------------
# GENEROWANIE PUNKTÓW I DEKLARACJI
# --------------------------------------------------------

def generate_declarations(Xc, Yc, Zc, D, N, A_const, B_max, C_max, Ch1, Ch2, Ch3, Ch4, Vrobot):
    R = D / 2.0
    decl_output = ""
    decl_output_aux = ""
    points = []

    for i in range(N):
        theta = 2 * math.pi * i / N
        theta2 = theta - math.pi/2
        X = Xc + R * math.cos(theta)
        Y = Yc + R * math.sin(theta)
        Z = Zc

        # 1. B i C jako parametry (NIE końcowe kąty)
        B = B_max
        C = C_max

        # 2. rotacja narzędzia
        R_tool = Ry(np.radians(B)) @ Rx(np.radians(C))

        # 3. lokalny układ okręgu
        tangent = np.array([-np.sin(theta2), np.cos(theta2), 0])
        normal = np.array([np.cos(theta2), np.sin(theta2), 0])
        binormal = np.array([0, 0, 1])

        R_frame = np.column_stack((tangent, normal, binormal))

        # 4. wektor bazowy
        v_base = np.array([0, 0, 1])

        # 5. FINALNY WEKTOR ORIENTACJI
        v = R_frame @ (R_tool @ v_base)

        A = np.degrees(np.arccos(v[2]))
        B = np.degrees(np.arccos(v[1])) - 90
        C = np.degrees(np.arccos(v[0])) + 90

        def wrap_180(x):
            return (x + 180) % 360 - 180

        C = wrap_180(C)

        wireFeed = Ch2
        robotVelocity = Vrobot / 60

        Pname = f"P{i+1}"
        points.append(Pname)

        # decl = (f"DECL E6POS XP{i + 1}={{X {X:.3f}, Y {Y:.3f}, Z {Z:.3f}, "
        #         f"A {A_const:.3f}, B {B:.4f}, C {C:.4f}, S 2, T 10}}\n"
        #         f"DECL FDAT FP{i + 1}={{TOOL_NO 6,BASE_NO 20,IPO_FRAME #BASE,POINT2[] \" \"}}\n"
        #         f"DECL LDAT LCPDAT{i + 1}={{VEL 0.200000,ACC 100.000,APO_DIST 500.000,APO_FAC 50.0000,AXIS_VEL 100.000,"
        #         f"AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0}}\n"
        #         f"DECL stArcDat_T WP{i + 1}={{WdatId[] \"WP{i + 1}\",Info {{Version 303030366}}}}\n")
        decl = (
            f"DECL E6POS XP{i + 1}={{X {X:.7f},Y {Y:.7f},Z {Z:.7f},"
            f"A {A_const:.7f},B {B:.7f},C {C:.7f},S 6,T 27,"
            f"E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}\n"

            f"DECL FDAT FP{i + 1}={{TOOL_NO 2,BASE_NO 20,IPO_FRAME #BASE,POINT2[] \" \"}}\n"

            f"DECL LDAT LCPDAT{i + 1}={{VEL 0.500000,ACC 100.000,APO_DIST 500.000,"
            f"APO_FAC 50.0000,AXIS_VEL 20.0000,AXIS_ACC 20.0000,ORI_TYP #VAR,CIRC_TYP #BASE,"
            f"JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0,"
            f"CB {{AUX_PT {{ORI #CONSIDER,E1 #CONSIDER,E2 #CONSIDER,E3 #CONSIDER,E4 #CONSIDER,E5 #CONSIDER,E6 #CONSIDER}},"
            f"TARGET_PT {{ORI #INTERPOLATE,E1 #INTERPOLATE,E2 #INTERPOLATE,E3 #INTERPOLATE,E4 #INTERPOLATE,E5 #INTERPOLATE,E6 #INTERPOLATE}}}}}}\n"

            f"DECL stArcDat_T WP{i + 1}={{WdatId[] \"WP{i + 1}\",Info {{Version 306040420}},Strike {{SeamName[] \" \",PartName[] \" \",SeamNumber 1,PartNumber 1,DesiredLength 0.0,LengthTolNeg 0.0,LengthTolPos 0.0,LengthCtrlActive FALSE}},Advanced {{BitCodedRobotMark 0}}}}\n"
        )
        declFirstPoint = (
            f"DECL E6POS XStart{i + 1}={{X {X:.7f},Y {Y:.7f},Z {Z:.7f},"
            f"A {A_const:.7f},B {B:.7f},C {C:.7f},S 6,T 27,"
            f"E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}\n"
        )
        # strike = (
        #     f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Strike {JobModeId[] \"GMAW synergic S2-Step\","
        #     "ParamSetId[] "f"\"Set1\""f",StartTime 0.500000,PreFlowTime 1.00000,Channel1 3449.00,Channel2 {wireFeed},Channel3 0.0,"
        #     "Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,PurgeTime 0.0},"
        #     "Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "f"\"Set2\""","
        #     f"Velocity {robotVelocity},Channel1 {Ch1},Channel2 {wireFeed},Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,"
        #     "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,"
        #     "Angle 0.0,LeftSideDelay 0.0,RightSideDelay 0.0}}\n")
        strike = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] \"WDAT{i + 1}\","
            f"Info {{Version 306040420,WId 1,WName[] \"Fronius TPSi cmd value\"}},"

            f"Strike {{JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] \"Set1\","
            f"StartTime 0.500000,PreFlowTime 1.00000,Channel1 3449.00,Channel2 {wireFeed},"
            f"Channel3 0.0,Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,"
            f"PurgeTime 0.0}},"

            f"Weld {{JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] \"Set2\","
            f"Velocity {robotVelocity},Channel1 {Ch1},Channel2 {wireFeed},"
            f"Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0}},"

            f"Weave {{Pattern #None,Length 4.00000,Amplitude 2.00000,Angle 0.0,"
            f"Frequency 2.00000,LeftSideDelay 0.0,RightSideDelay 0.0}}}}\n"
        )
        # weld = (
        #     f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "
        #     ""f"\"Set2\""f",Velocity {robotVelocity},Channel1 {Ch1},Channel2 {wireFeed},Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,"
        #     "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,Angle 0.0,"
        #     "LeftSideDelay 0.0,RightSideDelay 0.0}}\n")
        weld = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] \"WDAT{i + 1}\","
            f"Info {{Version 306040420,WId 1,WName[] \"Fronius TPSi cmd value\"}},"

            f"Weld {{JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] \"Set2\","
            f"Velocity {robotVelocity},Channel1 {Ch1},Channel2 {wireFeed},"
            f"Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0}},"

            f"Weave {{Pattern #None,Length 4.00000,Amplitude 2.00000,Angle 0.0,"
            f"Frequency 2.00000,LeftSideDelay 0.0,RightSideDelay 0.0}}}}\n"
        )
        # crater = (
        #     f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] "f"\"WDAT{i + 1}\""",Crater {JobModeId[] \"GMAW synergic S2-Step\","
        #     "ParamSetId[] "f"\"Set1\""f",CraterTime 0.500000,PostflowTime 1.00000,Channel1 {Ch1},Channel2 {wireFeed},"
        #     f"Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,"
        #     "BurnBackTime 0.0}}\n")
        crater = (
            f"DECL stArcDat_T WDAT{i + 1}={{WdatId[] \"WDAT{i + 1}\","
            f"Info {{Version 306040420,WId 1,WName[] \"Fronius TPSi cmd value\"}},"

            f"Crater {{JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] \"Set1\","
            f"CraterTime 0.500000,PostflowTime 1.00000,Channel1 {Ch1},Channel2 {wireFeed},"
            f"Channel3 {Ch3},Channel4 {Ch4},Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,"
            f"BurnBackTime 0.0}}}}\n"
        )
        if i == 0:
            decl += (strike)
        elif i == N - 1:
            decl += (crater)
        else:
            decl += (weld)

        decl_output += decl + "\n"
        decl_output_aux += declFirstPoint

    return decl_output_aux + "\n" + decl_output, points


# --------------------------------------------------------
# SZABLONY PROGRAMU
# --------------------------------------------------------
template_ARCON = """
;FOLD ARCON WDAT{I} LIN {P} Vel=0.5 m/s CPDAT{I} Tool[2]:Pipe Base[20]:LEGS ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arconlin; Kuka.IsGlobalPoint=False; Kuka.PointName={P}; Kuka.BlendingEnabled=False; Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.5; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; ArcTech.WdatVarName=WDAT{I}; ArcTech.Basic=3.6.4.420
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, 0.5)
SET_CD_PARAMS (0)
TRIGGER WHEN DISTANCE = 1 DELAY = ArcGetDelay(#PreDefinition, WDAT{I}) DO ArcMainNG(#PreDefinition, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = ArcGetDelay(#GasPreflow, WDAT{I}) DO ArcMainNG(#GasPreflow, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = ArcGetDelay(#ArcPreOn, WDAT{I}) DO ArcMainNG(#ArcOnMoveStd, WDAT{I}, W{P}) PRIO = -1 
ArcMainNG(#ArcOnBeforeMoveStd, WDAT{I}, W{P})
LIN X{P}
ArcMainNG(#ArcOnAfterMoveStd, WDAT{I}, W{P})
;ENDFOLD
"""

template_ARCSWI = """
;FOLD ARCSWI WDAT{I} SCIRC {Phelp} {P} CPDAT{I} Tool[2]:Pipe Base[20]:LEGS ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcswistandardscirc; Kuka.IsGlobalPoint=False; Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=True; Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.5; Kuka.VelocityFieldEnabled=True; Kuka.ColDetectFieldEnabled=True; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; IlfCommand=SCIRC; ArcTech.WdatVarName=WDAT{I}; ArcTech.Basic=3.6.4.420
;ENDFOLD
TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO ArcMainNG(#ArcSwiSplSingle, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
ArcMainNG(#ArcSwiBeforeSplSingle, WDAT{I}, W{P}, W{Phelp})
SCIRC X{Phelp}, X{P} WITH $VEL = SVEL_CP(gArcBasVelDefinition, , LCPDAT{I}), $TOOL = STOOL2(F{P}), $BASE = SBASE(F{P}.BASE_NO), $IPO_MODE = SIPO_MODE(F{P}.IPO_FRAME), $LOAD = SLOAD(F{P}.TOOL_NO), $ACC = SACC_CP(LCPDAT{I}), $ORI_TYPE = SORI_TYP(LCPDAT{I}), $CIRC_TYPE = SCIRC_TYP(LCPDAT{I}), $APO = SAPO(LCPDAT{I}), $APO.CDIS = wArcApoDistance, $CIRC_MODE = SCIRC_M(LCPDAT{I}), $JERK = SJERK(LCPDAT{I}), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0) C_Spl
ArcMainNG(#ArcSwiAfterSplSingle, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""

template_ARCOFF = """
;FOLD ARCOFF WDAT{I} SCIRC {Phelp} {P} CPDAT{I} Tool[2]:Pipe Base[20]:LEGS ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcoffstandardscirc; Kuka.IsGlobalPoint=False; Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=False; Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.5; Kuka.VelocityFieldEnabled=True; Kuka.ColDetectFieldEnabled=True; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; IlfCommand=SCIRC; ArcTech.WdatVarName=WDAT{I}; ArcTech.Basic=3.6.4.420
;ENDFOLD
TRIGGER WHEN PATH = ArcGetPath(#ArcOffBefore, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffBeforeOffSplSingle, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#ArcOffBefore2, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffBefOffSplSingle2, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOff, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffSplSingle, WDAT{I}, W{P}, W{Phelp}) PRIO = -1 
ArcMainNG(#ArcOffBeforeSplSingle, WDAT{I}, W{P}, W{Phelp})
SCIRC X{Phelp}, X{P} WITH $VEL = SVEL_CP(gArcBasVelDefinition, , LCPDAT{I}), $TOOL = STOOL2(F{P}), $BASE = SBASE(F{P}.BASE_NO), $IPO_MODE = SIPO_MODE(F{P}.IPO_FRAME), $LOAD = SLOAD(F{P}.TOOL_NO), $ACC = SACC_CP(LCPDAT{I}), $ORI_TYPE = SORI_TYP(LCPDAT{I}), $CIRC_TYPE = SCIRC_TYP(LCPDAT{I}), $APO = SAPO(LCPDAT{I}), $APO.CDIS = wArcApoDistance, $CIRC_MODE = SCIRC_M(LCPDAT{I}), $JERK = SJERK(LCPDAT{I}), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)
ArcMainNG(#ArcOffAfterSplSingle, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""

def generate_program(points):
    out = ""
    # ARCON
    out += template_ARCON.format(P=points[0], I=1)

    # ARCSWI (co drugi punkt)
    for i in range(2, len(points)-1, 2):
        out += template_ARCSWI.format(P=points[i], Phelp=points[i-1], I=i+1)

    # ARCOFF
    out += template_ARCOFF.format(P=points[-1], Phelp=points[-2], I=len(points))

    return out

SETTINGS_FILE = "settings.json"

def save_settings():
    data = {
        "Xc": entry_Xc.get(),
        "Yc": entry_Yc.get(),
        "Zc": entry_Zc.get(),
        "D": entry_D.get(),
        "N": entry_N.get(),
        "A_const": entry_A.get(),
        "B_max": entry_B.get(),
        "C_max": entry_C.get(),
        "Ch1": entry_Ch1.get(),
        "Ch2": entry_Ch2.get(),
        "Ch3": entry_Ch3.get(),
        "Ch4": entry_Ch4.get(),
        "Vrobot": entry_Vrobot.get()
    }
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f)


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return

    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)

    entry_Xc.delete(0, tk.END)
    entry_Xc.insert(0, data.get("Xc", ""))

    entry_Yc.delete(0, tk.END)
    entry_Yc.insert(0, data.get("Yc", ""))

    entry_Zc.delete(0, tk.END)
    entry_Zc.insert(0, data.get("Zc", ""))

    entry_D.delete(0, tk.END)
    entry_D.insert(0, data.get("D", ""))

    entry_N.delete(0, tk.END)
    entry_N.insert(0, data.get("N", ""))

    entry_A.delete(0, tk.END)
    entry_A.insert(0, data.get("A_const", ""))

    entry_B.delete(0, tk.END)
    entry_B.insert(0, data.get("B_max", ""))

    entry_C.delete(0, tk.END)
    entry_C.insert(0, data.get("C_max", ""))

    entry_Ch1.delete(0, tk.END)
    entry_Ch1.insert(0, data.get("Ch1", ""))

    entry_Ch2.delete(0, tk.END)
    entry_Ch2.insert(0, data.get("Ch2", ""))

    entry_Ch3.delete(0, tk.END)
    entry_Ch3.insert(0, data.get("Ch3", ""))

    entry_Ch4.delete(0, tk.END)
    entry_Ch4.insert(0, data.get("Ch4", ""))

    entry_Vrobot.delete(0, tk.END)
    entry_Vrobot.insert(0, data.get("Vrobot", ""))

# --------------------------------------------------------
# FUNKCJA WYWOŁYWANA PO KLIKNIĘCIU PRZYCISKU
# --------------------------------------------------------

def on_generate():
    Xc = float(entry_Xc.get())
    Yc = float(entry_Yc.get())
    Zc = float(entry_Zc.get())
    D = float(entry_D.get())
    N = int(entry_N.get())
    A_const = float(entry_A.get())
    B_max = float(entry_B.get())
    C_max = float(entry_C.get())
    Ch1 = float(entry_Ch1.get())
    Ch2 = float(entry_Ch2.get())
    Ch3 = float(entry_Ch3.get())
    Ch4= float(entry_Ch4.get())
    Vrobot= float(entry_Vrobot.get())

    declarations, points = generate_declarations(Xc, Yc, Zc, D, N, A_const, B_max, C_max, Ch1, Ch2, Ch3, Ch4, Vrobot)
    program = generate_program(points)

    text_decl.delete("1.0", tk.END)
    text_decl.insert(tk.END, declarations)

    text_prog.delete("1.0", tk.END)
    text_prog.insert(tk.END, program)


# --------------------------------------------------------
# GUI TKINTER
# --------------------------------------------------------


root = tk.Tk()
root.title("Generator KUKA ARC — GUI")

# ----- FRAME KONFIGURACJI (grid) -----
frame_cfg = ttk.Frame(root, padding=10)
frame_cfg.grid(row=0, column=0, sticky="nw")

labels = [
    "Xc", "Yc", "Zc", "Średnica D", "Liczba punktów N",
    "A_const", "B_max", "C_max",
    "Linia synergiczna (Channel1)",
    "Prędkość drutu [m/min] (Channel2)",
    "Korekta napięcia (Channel3)",
    "Korekta dynamiki (Channel4)",
    "Prędkość robota:"
]
defaults = ["123", "100.5", "-97", "20", "13", "-90", "25", "25",
            "3449.00",  # Channel1
            "6.0",      # Channel2
            "-2.0",     # Channel3
            "2.0",       # Channel4
            "0.25"
            ]
entries = []

buttonRow = 0
for i, (lbl, val) in enumerate(zip(labels, defaults)):
    ttk.Label(frame_cfg, text=lbl).grid(row=i, column=0, sticky="w")
    e = ttk.Entry(frame_cfg)
    e.insert(0, val)
    e.grid(row=i, column=1)
    entries.append(e)
    buttonRow = i + 1

(entry_Xc, entry_Yc, entry_Zc, entry_D, entry_N,
 entry_A, entry_B, entry_C,
 entry_Ch1, entry_Ch2, entry_Ch3,entry_Ch4,
 entry_Vrobot) = entries
load_settings()

ttk.Button(frame_cfg, text="GENERUJ", command=on_generate).grid(row=buttonRow, column=0, columnspan=2, pady=10)

# ----- FRAME WYNIKÓW (pack) -----
frame_out = ttk.Frame(root)
frame_out.grid(row=0, column=1, sticky="nsew")

# 🔴 TO JEST KLUCZOWE
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
frame_out.grid_rowconfigure(0, weight=1)
frame_out.grid_rowconfigure(1, weight=1)
frame_out.grid_columnconfigure(0, weight=1)

# ----- DECLARATIONS -----
frame_decl = ttk.Frame(frame_out)
frame_decl.pack(fill="both", expand=True, padx=10, pady=5)

scroll_decl = ttk.Scrollbar(frame_decl, orient="vertical")
scroll_decl.pack(side="right", fill="y")

text_decl = tk.Text(
    frame_decl,
    width=220,
    height=25,
    yscrollcommand=scroll_decl.set
)
text_decl.pack(side="left", fill="both", expand=True)

scroll_decl.config(command=text_decl.yview)

# ----- PROGRAM -----
frame_prog = ttk.Frame(frame_out)
frame_prog.pack(fill="both", expand=True, padx=10, pady=5)

scroll_prog = ttk.Scrollbar(frame_prog, orient="vertical")
scroll_prog.pack(side="right", fill="y")

text_prog = tk.Text(
    frame_prog,
    width=220,
    height=25,
    yscrollcommand=scroll_prog.set
)
text_prog.pack(side="left", fill="both", expand=True)

scroll_prog.config(command=text_prog.yview)


def on_closing():
    save_settings()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

