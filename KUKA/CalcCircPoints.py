import math

# ---------------------------------------------
# KONFIGURACJA
# ---------------------------------------------

# Środek okręgu
Xc = 123.000000
Yc = 99.500000
Zc = -97.0

# Średnica
D = 20.0
R = D / 2.0

# liczba punktów
N = 13

# Stała orientacja A
A_const = -90.0

# Maksymalne wartości zmian
B_max = 15
C_max = 15

# ---------------------------------------------
# GENEROWANIE PUNKTÓW
# ---------------------------------------------

for i in range(N):
    theta = 2 * math.pi * i / N

    X = Xc + R * math.cos(theta)
    Y = Yc + R * math.sin(theta)
    Z = Zc

    B = B_max * math.sin(theta)
    C = C_max * math.cos(theta)

    decl = (f"DECL E6POS XP{i+1}={{X {X:.3f}, Y {Y:.3f}, Z {Z:.3f}, "
          f"A {A_const:.3f}, B {B:.4f}, C {C:.4f}, S 2, T 10}}\n"
          f"DECL FDAT FP{i+1}={{TOOL_NO 6,BASE_NO 20,IPO_FRAME #BASE,POINT2[] \" \"}}\n"
          f"DECL LDAT LCPDAT{i+1}={{VEL 0.200000,ACC 100.000,APO_DIST 500.000,APO_FAC 50.0000,AXIS_VEL 100.000,"
          f"AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0}}\n"
          f"DECL stArcDat_T WP{i+1}={{WdatId[] "f"\"WP{i+1}\""",Info {Version 303030366}}\n")

    strile = (f"DECL stArcDat_T WDAT{i+1}={{WdatId[] "f"\"WDAT{i+1}\""",Strike {JobModeId[] \"GMAW synergic S2-Step\","
              "ParamSetId[] "f"\"Set1\""",StartTime 0.500000,PreFlowTime 1.00000,Channel1 3449.00,Channel2 6.00000,Channel3 0.0,"
              "Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,PurgeTime 0.0},"
              "Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "f"\"Set2\""","
              "Velocity 0.00330000,Channel1 3449.00,Channel2 6.00000,Channel3 0.0,Channel4 0.0,Channel5 0.0,"
              "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,"
              "Angle 0.0,LeftSideDelay 0.0,RightSideDelay 0.0}}\n")

    weld = (f"DECL stArcDat_T WDAT{i+1}={{WdatId[] "f"\"WDAT{i+1}\""",Weld {JobModeId[] \"GMAW synergic S2-Step\",ParamSetId[] "
            ""f"\"Set2\""",Velocity 0.00330000,Channel1 3449.00,Channel2 6.00000,Channel3 0.0,Channel4 0.0,Channel5 0.0,"
            "Channel6 0.0,Channel7 0.0,Channel8 0.0},Weave {Pattern #None,Length 4.00000,Amplitude 2.00000,Angle 0.0,"
            "LeftSideDelay 0.0,RightSideDelay 0.0}}\n")

    crater = (f"DECL stArcDat_T WDAT{i+1}={{WdatId[] "f"\"WDAT{i+1}\""",Crater {JobModeId[] \"GMAW synergic S2-Step\","
              "ParamSetId[] "f"\"Set1\""",CraterTime 0.500000,PostflowTime 1.00000,Channel1 3449.00,Channel2 6.00000,"
              "Channel3 0.0,Channel4 0.0,Channel5 0.0,Channel6 0.0,Channel7 0.0,Channel8 0.0,BurnBackTime 0.0}}\n")

    if i == 0:
        print(decl+strile)
    elif i == N:
        print(decl + crater)
    else:
        print(decl + weld)

# --------------------------------------------------------
# TEMPLATES
# --------------------------------------------------------

template_ARCON = """
;FOLD ARCON WDAT{I} LIN {P} Vel=0.2 m/s CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arconlin; Kuka.IsGlobalPoint=False; 
;Kuka.PointName={P}; Kuka.BlendingEnabled=False; Kuka.MoveDataName=CPDAT{I};
;Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True;
;ArcTech.WdatVarName=WDAT{I}; ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, 0.2)
SET_CD_PARAMS (0)
TRIGGER WHEN DISTANCE = 1 DELAY = ArcGetDelay(#PreDefinition, WDAT{I}) DO ArcMainNG(#PreDefinition, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = ArcGetDelay(#GasPreflow, WDAT{I}) DO ArcMainNG(#GasPreflow, WDAT{I}, W{P}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOn, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOnMoveStd, WDAT{I}, W{P}) PRIO = -1 
ArcMainNG(#ArcOnBeforeMoveStd, WDAT{I}, W{P})
LIN X{P}
ArcMainNG(#ArcOnAfterMoveStd, WDAT{I}, W{P})
;ENDFOLD
"""


template_ARCSWI = """
;FOLD ARCSWI WDAT{I} CIRC {Phelp} {P} CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcswicirc; Kuka.IsGlobalPoint=False;
;Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=True;
;Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0;
;Kuka.MovementParameterFieldEnabled=True; ArcTech.WdatVarName=WDAT{I};
;ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, gArcBasVelDefinition)
SET_CD_PARAMS (0)
TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO ArcMainNG(#ArcSwiMoveStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
ArcMainNG(#ArcSwiBeforeMoveStd, WDAT{I}, W{P}, W{Phelp})
CIRC X{Phelp}, X{P} C_Dis C_Dis
ArcMainNG(#ArcSwiAfterMoveStd, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""

template_ARCOFF = """
;FOLD ARCOFF WDAT{I} CIRC {Phelp} {P} CPDAT{I} Tool[6]:Fajka45 Base[20]:PP_noga ;%{{PE}}
;FOLD Parameters ;%{{h}}
;Params IlfProvider=kukaroboter.arctech.arcoffcirc; Kuka.IsGlobalPoint=False;
;Kuka.PointName={P}; Kuka.HelpPointName={Phelp}; Kuka.BlendingEnabled=False;
;Kuka.MoveDataName=CPDAT{I}; Kuka.VelocityPath=0.2; Kuka.CurrentCDSetIndex=0;
;Kuka.MovementParameterFieldEnabled=True; ArcTech.WdatVarName=WDAT{I}; 
;ArcTech.Basic=3.3.3.366
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT{I}
FDAT_ACT = F{P}
BAS(#CP_PARAMS, gArcBasVelDefinition)
SET_CD_PARAMS (0)
TRIGGER WHEN PATH = ArcGetPath(#ArcOffBefore, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffBeforeOffStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1
TRIGGER WHEN PATH = ArcGetPath(#OnTheFlyArcOff, WDAT{I}) DELAY = 0 DO ArcMainNG(#ArcOffMoveStd, WDAT{I}, W{P}, W{Phelp}) PRIO = -1 
ArcMainNG(#ArcOffBeforeMoveStd, WDAT{I}, W{P}, W{Phelp})
CIRC X{Phelp}, X{P}
ArcMainNG(#ArcOffAfterMoveStd, WDAT{I}, W{P}, W{Phelp})
;ENDFOLD
"""


# --------------------------------------------------------
# FUNKCJA GENERUJĄCA CAŁY PROGRAM
# --------------------------------------------------------

def generate_arc_program(point_list):
    out = ""

    # 1. ARCON
    P = point_list[0]
    out += template_ARCON.format(P=P, I=1)

    # 2. ARCSWI
    for i in range(2, len(point_list)-1,2):
        Phelp = point_list[i-1]
        P = point_list[i]
        out += template_ARCSWI.format(P=P, Phelp=Phelp, I=i+1)

    # 3. ARCOFF
    Phelp = point_list[-2]
    P = point_list[-1]
    out += template_ARCOFF.format(P=P, Phelp=Phelp, I=len(point_list))

    return out


# --------------------------------------------------------
# UŻYCIE
# --------------------------------------------------------

points = [f"P{i}" for i in range(1, N+1)]
program = generate_arc_program(points)

print(program)
