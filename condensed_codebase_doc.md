# Python Codebase Documentation

**Root Directory:** `/home/ec2-user/SageMaker/green-agent-age-of-inference-ii`
**Total Python Files:** 28

---

## 📂 Project Structure

```
📁 green-agent-age-of-inference-ii/
├── 📁 data/
│   ├── 📁 interviews/
│   │   ├── 📄 interview_metadata.json
│   │   ├── 📄 persona_001_trace.json
│   │   ├── 📄 persona_002_trace.json
│   │   ├── 📄 persona_003_trace.json
│   │   ├── 📄 persona_004_trace.json
│   │   ├── 📄 persona_005_trace.json
│   │   ├── 📄 persona_006_trace.json
│   │   ├── 📄 persona_007_trace.json
│   │   ├── 📄 persona_008_trace.json
│   │   ├── 📄 persona_009_trace.json
│   │   ├── 📄 persona_010_trace.json
│   │   ├── 📄 persona_011_trace.json
│   │   ├── 📄 persona_012_trace.json
│   │   ├── 📄 persona_013_trace.json
│   │   ├── 📄 persona_014_trace.json
│   │   ├── 📄 persona_015_trace.json
│   │   ├── 📄 persona_016_trace.json
│   │   ├── 📄 persona_017_trace.json
│   │   ├── 📄 persona_018_trace.json
│   │   ├── 📄 persona_019_trace.json
│   │   ├── 📄 persona_020_trace.json
│   │   ├── 📄 persona_021_trace.json
│   │   ├── 📄 persona_022_trace.json
│   │   ├── 📄 persona_023_trace.json
│   │   ├── 📄 persona_024_trace.json
│   │   ├── 📄 persona_025_trace.json
│   │   ├── 📄 persona_026_trace.json
│   │   ├── 📄 persona_027_trace.json
│   │   ├── 📄 persona_028_trace.json
│   │   ├── 📄 persona_030_trace.json
│   │   ├── 📄 persona_031_trace.json
│   │   ├── 📄 persona_032_trace.json
│   │   ├── 📄 persona_033_trace.json
│   │   ├── 📄 persona_034_trace.json
│   │   ├── 📄 persona_035_trace.json
│   │   ├── 📄 persona_036_trace.json
│   │   ├── 📄 persona_037_trace.json
│   │   ├── 📄 persona_038_trace.json
│   │   └── 📄 persona_039_trace.json
│   ├── 📁 jobs/
│   │   ├── 📄 j0.md
│   │   ├── 📄 j1.md
│   │   ├── 📄 j10.md
│   │   ├── 📄 j100.md
│   │   ├── 📄 j101.md
│   │   ├── 📄 j102.md
│   │   ├── 📄 j103.md
│   │   ├── 📄 j104.md
│   │   ├── 📄 j105.md
│   │   ├── 📄 j106.md
│   │   ├── 📄 j107.md
│   │   ├── 📄 j108.md
│   │   ├── 📄 j109.md
│   │   ├── 📄 j11.md
│   │   ├── 📄 j110.md
│   │   ├── 📄 j111.md
│   │   ├── 📄 j112.md
│   │   ├── 📄 j113.md
│   │   ├── 📄 j114.md
│   │   ├── 📄 j115.md
│   │   ├── 📄 j116.md
│   │   ├── 📄 j117.md
│   │   ├── 📄 j118.md
│   │   ├── 📄 j119.md
│   │   ├── 📄 j12.md
│   │   ├── 📄 j120.md
│   │   ├── 📄 j121.md
│   │   ├── 📄 j122.md
│   │   ├── 📄 j123.md
│   │   ├── 📄 j124.md
│   │   ├── 📄 j125.md
│   │   ├── 📄 j126.md
│   │   ├── 📄 j127.md
│   │   ├── 📄 j128.md
│   │   ├── 📄 j129.md
│   │   ├── 📄 j13.md
│   │   ├── 📄 j130.md
│   │   ├── 📄 j131.md
│   │   ├── 📄 j132.md
│   │   ├── 📄 j133.md
│   │   ├── 📄 j134.md
│   │   ├── 📄 j135.md
│   │   ├── 📄 j136.md
│   │   ├── 📄 j137.md
│   │   ├── 📄 j138.md
│   │   ├── 📄 j139.md
│   │   ├── 📄 j14.md
│   │   ├── 📄 j140.md
│   │   ├── 📄 j141.md
│   │   ├── 📄 j142.md
│   │   ├── 📄 j143.md
│   │   ├── 📄 j144.md
│   │   ├── 📄 j145.md
│   │   ├── 📄 j146.md
│   │   ├── 📄 j147.md
│   │   ├── 📄 j148.md
│   │   ├── 📄 j149.md
│   │   ├── 📄 j15.md
│   │   ├── 📄 j150.md
│   │   ├── 📄 j151.md
│   │   ├── 📄 j152.md
│   │   ├── 📄 j153.md
│   │   ├── 📄 j154.md
│   │   ├── 📄 j155.md
│   │   ├── 📄 j156.md
│   │   ├── 📄 j157.md
│   │   ├── 📄 j158.md
│   │   ├── 📄 j159.md
│   │   ├── 📄 j16.md
│   │   ├── 📄 j160.md
│   │   ├── 📄 j161.md
│   │   ├── 📄 j162.md
│   │   ├── 📄 j163.md
│   │   ├── 📄 j164.md
│   │   ├── 📄 j165.md
│   │   ├── 📄 j166.md
│   │   ├── 📄 j167.md
│   │   ├── 📄 j168.md
│   │   ├── 📄 j169.md
│   │   ├── 📄 j17.md
│   │   ├── 📄 j170.md
│   │   ├── 📄 j171.md
│   │   ├── 📄 j172.md
│   │   ├── 📄 j173.md
│   │   ├── 📄 j174.md
│   │   ├── 📄 j175.md
│   │   ├── 📄 j176.md
│   │   ├── 📄 j177.md
│   │   ├── 📄 j178.md
│   │   ├── 📄 j179.md
│   │   ├── 📄 j18.md
│   │   ├── 📄 j180.md
│   │   ├── 📄 j181.md
│   │   ├── 📄 j182.md
│   │   ├── 📄 j183.md
│   │   ├── 📄 j184.md
│   │   ├── 📄 j185.md
│   │   ├── 📄 j186.md
│   │   ├── 📄 j187.md
│   │   ├── 📄 j188.md
│   │   ├── 📄 j189.md
│   │   ├── 📄 j19.md
│   │   ├── 📄 j190.md
│   │   ├── 📄 j191.md
│   │   ├── 📄 j192.md
│   │   ├── 📄 j193.md
│   │   ├── 📄 j194.md
│   │   ├── 📄 j195.md
│   │   ├── 📄 j196.md
│   │   ├── 📄 j197.md
│   │   ├── 📄 j198.md
│   │   ├── 📄 j199.md
│   │   ├── 📄 j2.md
│   │   ├── 📄 j20.md
│   │   ├── 📄 j21.md
│   │   ├── 📄 j22.md
│   │   ├── 📄 j23.md
│   │   ├── 📄 j24.md
│   │   ├── 📄 j25.md
│   │   ├── 📄 j26.md
│   │   ├── 📄 j27.md
│   │   ├── 📄 j28.md
│   │   ├── 📄 j29.md
│   │   ├── 📄 j3.md
│   │   ├── 📄 j30.md
│   │   ├── 📄 j31.md
│   │   ├── 📄 j32.md
│   │   ├── 📄 j33.md
│   │   ├── 📄 j34.md
│   │   ├── 📄 j35.md
│   │   ├── 📄 j36.md
│   │   ├── 📄 j37.md
│   │   ├── 📄 j38.md
│   │   ├── 📄 j39.md
│   │   ├── 📄 j4.md
│   │   ├── 📄 j40.md
│   │   ├── 📄 j41.md
│   │   ├── 📄 j42.md
│   │   ├── 📄 j43.md
│   │   ├── 📄 j44.md
│   │   ├── 📄 j45.md
│   │   ├── 📄 j46.md
│   │   ├── 📄 j47.md
│   │   ├── 📄 j48.md
│   │   ├── 📄 j49.md
│   │   ├── 📄 j5.md
│   │   ├── 📄 j50.md
│   │   ├── 📄 j51.md
│   │   ├── 📄 j52.md
│   │   ├── 📄 j53.md
│   │   ├── 📄 j54.md
│   │   ├── 📄 j55.md
│   │   ├── 📄 j56.md
│   │   ├── 📄 j57.md
│   │   ├── 📄 j58.md
│   │   ├── 📄 j59.md
│   │   ├── 📄 j6.md
│   │   ├── 📄 j60.md
│   │   ├── 📄 j61.md
│   │   ├── 📄 j62.md
│   │   ├── 📄 j63.md
│   │   ├── 📄 j64.md
│   │   ├── 📄 j65.md
│   │   ├── 📄 j66.md
│   │   ├── 📄 j67.md
│   │   ├── 📄 j68.md
│   │   ├── 📄 j69.md
│   │   ├── 📄 j7.md
│   │   ├── 📄 j70.md
│   │   ├── 📄 j71.md
│   │   ├── 📄 j72.md
│   │   ├── 📄 j73.md
│   │   ├── 📄 j74.md
│   │   ├── 📄 j75.md
│   │   ├── 📄 j76.md
│   │   ├── 📄 j77.md
│   │   ├── 📄 j78.md
│   │   ├── 📄 j79.md
│   │   ├── 📄 j8.md
│   │   ├── 📄 j80.md
│   │   ├── 📄 j81.md
│   │   ├── 📄 j82.md
│   │   ├── 📄 j83.md
│   │   ├── 📄 j84.md
│   │   ├── 📄 j85.md
│   │   ├── 📄 j86.md
│   │   ├── 📄 j87.md
│   │   ├── 📄 j88.md
│   │   ├── 📄 j89.md
│   │   ├── 📄 j9.md
│   │   ├── 📄 j90.md
│   │   ├── 📄 j91.md
│   │   ├── 📄 j92.md
│   │   ├── 📄 j93.md
│   │   ├── 📄 j94.md
│   │   ├── 📄 j95.md
│   │   ├── 📄 j96.md
│   │   ├── 📄 j97.md
│   │   ├── 📄 j98.md
│   │   └── 📄 j99.md
│   ├── 📁 profiles/
│   │   ├── 📄 persona_001.json
│   │   ├── 📄 persona_002.json
│   │   ├── 📄 persona_003.json
│   │   ├── 📄 persona_004.json
│   │   ├── 📄 persona_005.json
│   │   ├── 📄 persona_006.json
│   │   ├── 📄 persona_007.json
│   │   ├── 📄 persona_008.json
│   │   ├── 📄 persona_009.json
│   │   ├── 📄 persona_010.json
│   │   ├── 📄 persona_011.json
│   │   ├── 📄 persona_012.json
│   │   ├── 📄 persona_013.json
│   │   ├── 📄 persona_014.json
│   │   ├── 📄 persona_015.json
│   │   ├── 📄 persona_016.json
│   │   ├── 📄 persona_017.json
│   │   ├── 📄 persona_018.json
│   │   ├── 📄 persona_019.json
│   │   ├── 📄 persona_020.json
│   │   ├── 📄 persona_021.json
│   │   ├── 📄 persona_022.json
│   │   ├── 📄 persona_023.json
│   │   ├── 📄 persona_024.json
│   │   ├── 📄 persona_025.json
│   │   ├── 📄 persona_026.json
│   │   ├── 📄 persona_027.json
│   │   ├── 📄 persona_028.json
│   │   ├── 📄 persona_030.json
│   │   ├── 📄 persona_031.json
│   │   ├── 📄 persona_032.json
│   │   ├── 📄 persona_033.json
│   │   ├── 📄 persona_034.json
│   │   ├── 📄 persona_035.json
│   │   ├── 📄 persona_036.json
│   │   ├── 📄 persona_037.json
│   │   ├── 📄 persona_038.json
│   │   └── 📄 persona_039.json
│   ├── 📁 trainings/
│   │   ├── 📄 tr0.md
│   │   ├── 📄 tr1.md
│   │   ├── 📄 tr10.md
│   │   ├── 📄 tr100.md
│   │   ├── 📄 tr101.md
│   │   ├── 📄 tr102.md
│   │   ├── 📄 tr103.md
│   │   ├── 📄 tr104.md
│   │   ├── 📄 tr105.md
│   │   ├── 📄 tr106.md
│   │   ├── 📄 tr107.md
│   │   ├── 📄 tr108.md
│   │   ├── 📄 tr109.md
│   │   ├── 📄 tr11.md
│   │   ├── 📄 tr110.md
│   │   ├── 📄 tr111.md
│   │   ├── 📄 tr112.md
│   │   ├── 📄 tr113.md
│   │   ├── 📄 tr114.md
│   │   ├── 📄 tr115.md
│   │   ├── 📄 tr116.md
│   │   ├── 📄 tr117.md
│   │   ├── 📄 tr118.md
│   │   ├── 📄 tr119.md
│   │   ├── 📄 tr12.md
│   │   ├── 📄 tr120.md
│   │   ├── 📄 tr121.md
│   │   ├── 📄 tr122.md
│   │   ├── 📄 tr123.md
│   │   ├── 📄 tr124.md
│   │   ├── 📄 tr125.md
│   │   ├── 📄 tr126.md
│   │   ├── 📄 tr127.md
│   │   ├── 📄 tr128.md
│   │   ├── 📄 tr129.md
│   │   ├── 📄 tr13.md
│   │   ├── 📄 tr130.md
│   │   ├── 📄 tr131.md
│   │   ├── 📄 tr132.md
│   │   ├── 📄 tr133.md
│   │   ├── 📄 tr134.md
│   │   ├── 📄 tr135.md
│   │   ├── 📄 tr136.md
│   │   ├── 📄 tr137.md
│   │   ├── 📄 tr138.md
│   │   ├── 📄 tr139.md
│   │   ├── 📄 tr14.md
│   │   ├── 📄 tr140.md
│   │   ├── 📄 tr141.md
│   │   ├── 📄 tr142.md
│   │   ├── 📄 tr143.md
│   │   ├── 📄 tr144.md
│   │   ├── 📄 tr145.md
│   │   ├── 📄 tr146.md
│   │   ├── 📄 tr147.md
│   │   ├── 📄 tr148.md
│   │   ├── 📄 tr149.md
│   │   ├── 📄 tr15.md
│   │   ├── 📄 tr150.md
│   │   ├── 📄 tr151.md
│   │   ├── 📄 tr152.md
│   │   ├── 📄 tr153.md
│   │   ├── 📄 tr154.md
│   │   ├── 📄 tr155.md
│   │   ├── 📄 tr156.md
│   │   ├── 📄 tr157.md
│   │   ├── 📄 tr158.md
│   │   ├── 📄 tr159.md
│   │   ├── 📄 tr16.md
│   │   ├── 📄 tr160.md
│   │   ├── 📄 tr161.md
│   │   ├── 📄 tr162.md
│   │   ├── 📄 tr163.md
│   │   ├── 📄 tr164.md
│   │   ├── 📄 tr165.md
│   │   ├── 📄 tr166.md
│   │   ├── 📄 tr167.md
│   │   ├── 📄 tr168.md
│   │   ├── 📄 tr169.md
│   │   ├── 📄 tr17.md
│   │   ├── 📄 tr170.md
│   │   ├── 📄 tr171.md
│   │   ├── 📄 tr172.md
│   │   ├── 📄 tr173.md
│   │   ├── 📄 tr174.md
│   │   ├── 📄 tr175.md
│   │   ├── 📄 tr176.md
│   │   ├── 📄 tr177.md
│   │   ├── 📄 tr178.md
│   │   ├── 📄 tr179.md
│   │   ├── 📄 tr18.md
│   │   ├── 📄 tr180.md
│   │   ├── 📄 tr181.md
│   │   ├── 📄 tr182.md
│   │   ├── 📄 tr183.md
│   │   ├── 📄 tr184.md
│   │   ├── 📄 tr185.md
│   │   ├── 📄 tr186.md
│   │   ├── 📄 tr187.md
│   │   ├── 📄 tr188.md
│   │   ├── 📄 tr189.md
│   │   ├── 📄 tr19.md
│   │   ├── 📄 tr190.md
│   │   ├── 📄 tr191.md
│   │   ├── 📄 tr192.md
│   │   ├── 📄 tr193.md
│   │   ├── 📄 tr194.md
│   │   ├── 📄 tr195.md
│   │   ├── 📄 tr196.md
│   │   ├── 📄 tr197.md
│   │   ├── 📄 tr198.md
│   │   ├── 📄 tr199.md
│   │   ├── 📄 tr2.md
│   │   ├── 📄 tr20.md
│   │   ├── 📄 tr200.md
│   │   ├── 📄 tr201.md
│   │   ├── 📄 tr202.md
│   │   ├── 📄 tr203.md
│   │   ├── 📄 tr204.md
│   │   ├── 📄 tr205.md
│   │   ├── 📄 tr206.md
│   │   ├── 📄 tr207.md
│   │   ├── 📄 tr208.md
│   │   ├── 📄 tr209.md
│   │   ├── 📄 tr21.md
│   │   ├── 📄 tr210.md
│   │   ├── 📄 tr211.md
│   │   ├── 📄 tr212.md
│   │   ├── 📄 tr213.md
│   │   ├── 📄 tr214.md
│   │   ├── 📄 tr215.md
│   │   ├── 📄 tr216.md
│   │   ├── 📄 tr217.md
│   │   ├── 📄 tr218.md
│   │   ├── 📄 tr219.md
│   │   ├── 📄 tr22.md
│   │   ├── 📄 tr220.md
│   │   ├── 📄 tr221.md
│   │   ├── 📄 tr222.md
│   │   ├── 📄 tr223.md
│   │   ├── 📄 tr224.md
│   │   ├── 📄 tr225.md
│   │   ├── 📄 tr226.md
│   │   ├── 📄 tr227.md
│   │   ├── 📄 tr228.md
│   │   ├── 📄 tr229.md
│   │   ├── 📄 tr23.md
│   │   ├── 📄 tr230.md
│   │   ├── 📄 tr231.md
│   │   ├── 📄 tr232.md
│   │   ├── 📄 tr233.md
│   │   ├── 📄 tr234.md
│   │   ├── 📄 tr235.md
│   │   ├── 📄 tr236.md
│   │   ├── 📄 tr237.md
│   │   ├── 📄 tr238.md
│   │   ├── 📄 tr239.md
│   │   ├── 📄 tr24.md
│   │   ├── 📄 tr240.md
│   │   ├── 📄 tr241.md
│   │   ├── 📄 tr242.md
│   │   ├── 📄 tr243.md
│   │   ├── 📄 tr244.md
│   │   ├── 📄 tr245.md
│   │   ├── 📄 tr246.md
│   │   ├── 📄 tr247.md
│   │   ├── 📄 tr248.md
│   │   ├── 📄 tr249.md
│   │   ├── 📄 tr25.md
│   │   ├── 📄 tr250.md
│   │   ├── 📄 tr251.md
│   │   ├── 📄 tr252.md
│   │   ├── 📄 tr253.md
│   │   ├── 📄 tr254.md
│   │   ├── 📄 tr255.md
│   │   ├── 📄 tr256.md
│   │   ├── 📄 tr257.md
│   │   ├── 📄 tr258.md
│   │   ├── 📄 tr259.md
│   │   ├── 📄 tr26.md
│   │   ├── 📄 tr260.md
│   │   ├── 📄 tr261.md
│   │   ├── 📄 tr262.md
│   │   ├── 📄 tr263.md
│   │   ├── 📄 tr264.md
│   │   ├── 📄 tr265.md
│   │   ├── 📄 tr266.md
│   │   ├── 📄 tr267.md
│   │   ├── 📄 tr268.md
│   │   ├── 📄 tr269.md
│   │   ├── 📄 tr27.md
│   │   ├── 📄 tr270.md
│   │   ├── 📄 tr271.md
│   │   ├── 📄 tr272.md
│   │   ├── 📄 tr273.md
│   │   ├── 📄 tr274.md
│   │   ├── 📄 tr275.md
│   │   ├── 📄 tr276.md
│   │   ├── 📄 tr277.md
│   │   ├── 📄 tr278.md
│   │   ├── 📄 tr279.md
│   │   ├── 📄 tr28.md
│   │   ├── 📄 tr280.md
│   │   ├── 📄 tr281.md
│   │   ├── 📄 tr282.md
│   │   ├── 📄 tr283.md
│   │   ├── 📄 tr284.md
│   │   ├── 📄 tr285.md
│   │   ├── 📄 tr286.md
│   │   ├── 📄 tr287.md
│   │   ├── 📄 tr288.md
│   │   ├── 📄 tr289.md
│   │   ├── 📄 tr29.md
│   │   ├── 📄 tr290.md
│   │   ├── 📄 tr291.md
│   │   ├── 📄 tr292.md
│   │   ├── 📄 tr293.md
│   │   ├── 📄 tr294.md
│   │   ├── 📄 tr295.md
│   │   ├── 📄 tr296.md
│   │   ├── 📄 tr297.md
│   │   ├── 📄 tr298.md
│   │   ├── 📄 tr299.md
│   │   ├── 📄 tr3.md
│   │   ├── 📄 tr30.md
│   │   ├── 📄 tr300.md
│   │   ├── 📄 tr301.md
│   │   ├── 📄 tr302.md
│   │   ├── 📄 tr303.md
│   │   ├── 📄 tr304.md
│   │   ├── 📄 tr305.md
│   │   ├── 📄 tr306.md
│   │   ├── 📄 tr307.md
│   │   ├── 📄 tr308.md
│   │   ├── 📄 tr309.md
│   │   ├── 📄 tr31.md
│   │   ├── 📄 tr310.md
│   │   ├── 📄 tr311.md
│   │   ├── 📄 tr312.md
│   │   ├── 📄 tr313.md
│   │   ├── 📄 tr314.md
│   │   ├── 📄 tr315.md
│   │   ├── 📄 tr316.md
│   │   ├── 📄 tr317.md
│   │   ├── 📄 tr318.md
│   │   ├── 📄 tr319.md
│   │   ├── 📄 tr32.md
│   │   ├── 📄 tr320.md
│   │   ├── 📄 tr321.md
│   │   ├── 📄 tr322.md
│   │   ├── 📄 tr323.md
│   │   ├── 📄 tr324.md
│   │   ├── 📄 tr325.md
│   │   ├── 📄 tr326.md
│   │   ├── 📄 tr327.md
│   │   ├── 📄 tr328.md
│   │   ├── 📄 tr329.md
│   │   ├── 📄 tr33.md
│   │   ├── 📄 tr330.md
│   │   ├── 📄 tr331.md
│   │   ├── 📄 tr332.md
│   │   ├── 📄 tr333.md
│   │   ├── 📄 tr334.md
│   │   ├── 📄 tr335.md
│   │   ├── 📄 tr336.md
│   │   ├── 📄 tr337.md
│   │   ├── 📄 tr338.md
│   │   ├── 📄 tr339.md
│   │   ├── 📄 tr34.md
│   │   ├── 📄 tr340.md
│   │   ├── 📄 tr341.md
│   │   ├── 📄 tr342.md
│   │   ├── 📄 tr343.md
│   │   ├── 📄 tr344.md
│   │   ├── 📄 tr345.md
│   │   ├── 📄 tr346.md
│   │   ├── 📄 tr347.md
│   │   ├── 📄 tr348.md
│   │   ├── 📄 tr349.md
│   │   ├── 📄 tr35.md
│   │   ├── 📄 tr350.md
│   │   ├── 📄 tr351.md
│   │   ├── 📄 tr352.md
│   │   ├── 📄 tr353.md
│   │   ├── 📄 tr354.md
│   │   ├── 📄 tr355.md
│   │   ├── 📄 tr356.md
│   │   ├── 📄 tr357.md
│   │   ├── 📄 tr358.md
│   │   ├── 📄 tr359.md
│   │   ├── 📄 tr36.md
│   │   ├── 📄 tr360.md
│   │   ├── 📄 tr361.md
│   │   ├── 📄 tr362.md
│   │   ├── 📄 tr363.md
│   │   ├── 📄 tr364.md
│   │   ├── 📄 tr365.md
│   │   ├── 📄 tr366.md
│   │   ├── 📄 tr367.md
│   │   ├── 📄 tr368.md
│   │   ├── 📄 tr369.md
│   │   ├── 📄 tr37.md
│   │   ├── 📄 tr370.md
│   │   ├── 📄 tr371.md
│   │   ├── 📄 tr372.md
│   │   ├── 📄 tr373.md
│   │   ├── 📄 tr374.md
│   │   ├── 📄 tr375.md
│   │   ├── 📄 tr376.md
│   │   ├── 📄 tr377.md
│   │   ├── 📄 tr378.md
│   │   ├── 📄 tr379.md
│   │   ├── 📄 tr38.md
│   │   ├── 📄 tr380.md
│   │   ├── 📄 tr381.md
│   │   ├── 📄 tr382.md
│   │   ├── 📄 tr383.md
│   │   ├── 📄 tr384.md
│   │   ├── 📄 tr385.md
│   │   ├── 📄 tr386.md
│   │   ├── 📄 tr387.md
│   │   ├── 📄 tr388.md
│   │   ├── 📄 tr389.md
│   │   ├── 📄 tr39.md
│   │   ├── 📄 tr390.md
│   │   ├── 📄 tr391.md
│   │   ├── 📄 tr392.md
│   │   ├── 📄 tr393.md
│   │   ├── 📄 tr394.md
│   │   ├── 📄 tr395.md
│   │   ├── 📄 tr396.md
│   │   ├── 📄 tr397.md
│   │   ├── 📄 tr398.md
│   │   ├── 📄 tr399.md
│   │   ├── 📄 tr4.md
│   │   ├── 📄 tr40.md
│   │   ├── 📄 tr400.md
│   │   ├── 📄 tr401.md
│   │   ├── 📄 tr402.md
│   │   ├── 📄 tr403.md
│   │   ├── 📄 tr404.md
│   │   ├── 📄 tr405.md
│   │   ├── 📄 tr406.md
│   │   ├── 📄 tr407.md
│   │   ├── 📄 tr408.md
│   │   ├── 📄 tr409.md
│   │   ├── 📄 tr41.md
│   │   ├── 📄 tr410.md
│   │   ├── 📄 tr411.md
│   │   ├── 📄 tr412.md
│   │   ├── 📄 tr413.md
│   │   ├── 📄 tr414.md
│   │   ├── 📄 tr415.md
│   │   ├── 📄 tr416.md
│   │   ├── 📄 tr417.md
│   │   ├── 📄 tr418.md
│   │   ├── 📄 tr419.md
│   │   ├── 📄 tr42.md
│   │   ├── 📄 tr420.md
│   │   ├── 📄 tr421.md
│   │   ├── 📄 tr422.md
│   │   ├── 📄 tr423.md
│   │   ├── 📄 tr424.md
│   │   ├── 📄 tr425.md
│   │   ├── 📄 tr426.md
│   │   ├── 📄 tr427.md
│   │   ├── 📄 tr428.md
│   │   ├── 📄 tr429.md
│   │   ├── 📄 tr43.md
│   │   ├── 📄 tr430.md
│   │   ├── 📄 tr431.md
│   │   ├── 📄 tr432.md
│   │   ├── 📄 tr433.md
│   │   ├── 📄 tr434.md
│   │   ├── 📄 tr435.md
│   │   ├── 📄 tr436.md
│   │   ├── 📄 tr437.md
│   │   ├── 📄 tr438.md
│   │   ├── 📄 tr439.md
│   │   ├── 📄 tr44.md
│   │   ├── 📄 tr440.md
│   │   ├── 📄 tr441.md
│   │   ├── 📄 tr442.md
│   │   ├── 📄 tr443.md
│   │   ├── 📄 tr444.md
│   │   ├── 📄 tr445.md
│   │   ├── 📄 tr446.md
│   │   ├── 📄 tr447.md
│   │   ├── 📄 tr448.md
│   │   ├── 📄 tr449.md
│   │   ├── 📄 tr45.md
│   │   ├── 📄 tr450.md
│   │   ├── 📄 tr451.md
│   │   ├── 📄 tr452.md
│   │   ├── 📄 tr453.md
│   │   ├── 📄 tr454.md
│   │   ├── 📄 tr455.md
│   │   ├── 📄 tr456.md
│   │   ├── 📄 tr457.md
│   │   ├── 📄 tr458.md
│   │   ├── 📄 tr459.md
│   │   ├── 📄 tr46.md
│   │   ├── 📄 tr460.md
│   │   ├── 📄 tr461.md
│   │   ├── 📄 tr462.md
│   │   ├── 📄 tr463.md
│   │   ├── 📄 tr464.md
│   │   ├── 📄 tr465.md
│   │   ├── 📄 tr466.md
│   │   ├── 📄 tr467.md
│   │   ├── 📄 tr468.md
│   │   ├── 📄 tr469.md
│   │   ├── 📄 tr47.md
│   │   ├── 📄 tr470.md
│   │   ├── 📄 tr471.md
│   │   ├── 📄 tr472.md
│   │   ├── 📄 tr473.md
│   │   ├── 📄 tr474.md
│   │   ├── 📄 tr475.md
│   │   ├── 📄 tr476.md
│   │   ├── 📄 tr477.md
│   │   ├── 📄 tr478.md
│   │   ├── 📄 tr479.md
│   │   ├── 📄 tr48.md
│   │   ├── 📄 tr480.md
│   │   ├── 📄 tr481.md
│   │   ├── 📄 tr482.md
│   │   ├── 📄 tr483.md
│   │   ├── 📄 tr484.md
│   │   ├── 📄 tr485.md
│   │   ├── 📄 tr486.md
│   │   ├── 📄 tr487.md
│   │   ├── 📄 tr488.md
│   │   ├── 📄 tr489.md
│   │   ├── 📄 tr49.md
│   │   ├── 📄 tr490.md
│   │   ├── 📄 tr491.md
│   │   ├── 📄 tr492.md
│   │   ├── 📄 tr493.md
│   │   ├── 📄 tr494.md
│   │   ├── 📄 tr495.md
│   │   ├── 📄 tr496.md
│   │   ├── 📄 tr5.md
│   │   ├── 📄 tr50.md
│   │   ├── 📄 tr51.md
│   │   ├── 📄 tr52.md
│   │   ├── 📄 tr53.md
│   │   ├── 📄 tr54.md
│   │   ├── 📄 tr55.md
│   │   ├── 📄 tr56.md
│   │   ├── 📄 tr57.md
│   │   ├── 📄 tr58.md
│   │   ├── 📄 tr59.md
│   │   ├── 📄 tr6.md
│   │   ├── 📄 tr60.md
│   │   ├── 📄 tr61.md
│   │   ├── 📄 tr62.md
│   │   ├── 📄 tr63.md
│   │   ├── 📄 tr64.md
│   │   ├── 📄 tr65.md
│   │   ├── 📄 tr66.md
│   │   ├── 📄 tr67.md
│   │   ├── 📄 tr68.md
│   │   ├── 📄 tr69.md
│   │   ├── 📄 tr7.md
│   │   ├── 📄 tr70.md
│   │   ├── 📄 tr71.md
│   │   ├── 📄 tr72.md
│   │   ├── 📄 tr73.md
│   │   ├── 📄 tr74.md
│   │   ├── 📄 tr75.md
│   │   ├── 📄 tr76.md
│   │   ├── 📄 tr77.md
│   │   ├── 📄 tr78.md
│   │   ├── 📄 tr79.md
│   │   ├── 📄 tr8.md
│   │   ├── 📄 tr80.md
│   │   ├── 📄 tr81.md
│   │   ├── 📄 tr82.md
│   │   ├── 📄 tr83.md
│   │   ├── 📄 tr84.md
│   │   ├── 📄 tr85.md
│   │   ├── 📄 tr86.md
│   │   ├── 📄 tr87.md
│   │   ├── 📄 tr88.md
│   │   ├── 📄 tr89.md
│   │   ├── 📄 tr9.md
│   │   ├── 📄 tr90.md
│   │   ├── 📄 tr91.md
│   │   ├── 📄 tr92.md
│   │   ├── 📄 tr93.md
│   │   ├── 📄 tr94.md
│   │   ├── 📄 tr95.md
│   │   ├── 📄 tr96.md
│   │   ├── 📄 tr97.md
│   │   ├── 📄 tr98.md
│   │   └── 📄 tr99.md
│   ├── 📄 parsed_jobs.json
│   ├── 📄 parsed_trainings.json
│   └── 📄 parsing_metadata.json
├── 📁 docs/
│   ├── 📄 ai_coding_instructions.md
│   ├── 📄 condensed_codebase_doc.md
│   ├── 📄 design.md
│   ├── 📄 design_v2.md
│   ├── 📄 design_v3.md
│   ├── 📄 development_environment.md
│   ├── 📄 GDSC API Documentation.md
│   ├── 📄 learning_log.md
│   ├── 📄 pocketflow.md
│   ├── 📄 scoring_system.md
│   └── 📄 terminal_training.md
├── 📁 notebooks/
│   ├── 📄 01_data_exploration.ipynb
│   └── 📄 01_data_exploration.md
├── 📁 output/
│   ├── 📁 logs/
│   │   ├── 📄 persona_001_trace.json
│   │   ├── 📄 persona_002_trace.json
│   │   ├── 📄 persona_003_trace.json
│   │   ├── 📄 persona_004_trace.json
│   │   └── 📄 persona_005_trace.json
│   └── 📄 submission.json
├── 📁 pocketflow/
│   ├── 📁 __pycache__/
│   │   └── 📄 __init__.cpython-310.pyc
│   ├── 🐍 __init__.py
│   └── 📄 __init__.pyi
├── 📁 src/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-310.pyc
│   │   ├── 📄 flow.cpython-310.pyc
│   │   ├── 📄 main.cpython-310.pyc
│   │   └── 📄 nodes.cpython-310.pyc
│   ├── 📁 utils/
│   │   ├── 📁 __pycache__/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 call_llm.py
│   │   ├── 🐍 data_retrieval.py
│   │   ├── 🐍 gdsc_utils.py
│   │   ├── 🐍 matching_rules.py
│   │   └── 🐍 s3_helper.py
│   ├── 🐍 __init__.py
│   ├── 🐍 flow.py
│   ├── 🐍 flow_old.py
│   └── 🐍 nodes.py
├── 📁 tests/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-310.pyc
│   │   ├── 📄 test_integration.cpython-310-pytest-8.4.2.pyc
│   │   ├── 📄 test_matching_rules.cpython-310-pytest-8.4.2.pyc
│   │   └── 📄 test_nodes.cpython-310-pytest-8.4.2.pyc
│   ├── 🐍 __init__.py
│   ├── 🐍 test_call_llm.py
│   ├── 🐍 test_data_retrieval.py
│   ├── 🐍 test_integration.py
│   ├── 🐍 test_matching.py
│   ├── 🐍 test_matching_rules.py
│   ├── 🐍 test_nodes.py
│   └── 🐍 test_utils.py
├── 🐍 analyze_parsed_data.py
├── 📄 codebase_documentation.md
├── 🐍 collect_python_codebase_info.py
├── 🐍 collect_python_codebase_info_v2.py
├── 📄 condensed_codebase_doc.md
├── 🐍 conduct_interviews.py
├── 🐍 conduct_interviews_old.py
├── 🐍 generate_recommendations.py
├── 🐍 generic_s3_downloader.py
├── 📄 LICENSE
├── 🐍 main.py
├── 🐍 parse_data.py
├── 📄 pyproject.toml
├── 📄 README.md
├── 📄 run_startup.sh
├── 📄 test_notebook.ipynb
└── 📄 uv.lock
```

---

## 📑 Table of Contents

1. [green-agent-age-of-inference-ii/analyze_parsed_data.py](#green-agent-age-of-inference-ii-analyze_parsed_data-py)
2. [green-agent-age-of-inference-ii/collect_python_codebase_info.py](#green-agent-age-of-inference-ii-collect_python_codebase_info-py)
3. [green-agent-age-of-inference-ii/collect_python_codebase_info_v2.py](#green-agent-age-of-inference-ii-collect_python_codebase_info_v2-py)
4. [green-agent-age-of-inference-ii/conduct_interviews.py](#green-agent-age-of-inference-ii-conduct_interviews-py)
5. [green-agent-age-of-inference-ii/conduct_interviews_old.py](#green-agent-age-of-inference-ii-conduct_interviews_old-py)
6. [green-agent-age-of-inference-ii/generate_recommendations.py](#green-agent-age-of-inference-ii-generate_recommendations-py)
7. [green-agent-age-of-inference-ii/generic_s3_downloader.py](#green-agent-age-of-inference-ii-generic_s3_downloader-py)
8. [green-agent-age-of-inference-ii/main.py](#green-agent-age-of-inference-ii-main-py)
9. [green-agent-age-of-inference-ii/parse_data.py](#green-agent-age-of-inference-ii-parse_data-py)
10. [green-agent-age-of-inference-ii/pocketflow/__init__.py](#green-agent-age-of-inference-ii-pocketflow-__init__-py)
11. [green-agent-age-of-inference-ii/src/__init__.py](#green-agent-age-of-inference-ii-src-__init__-py)
12. [green-agent-age-of-inference-ii/src/flow.py](#green-agent-age-of-inference-ii-src-flow-py)
13. [green-agent-age-of-inference-ii/src/flow_old.py](#green-agent-age-of-inference-ii-src-flow_old-py)
14. [green-agent-age-of-inference-ii/src/nodes.py](#green-agent-age-of-inference-ii-src-nodes-py)
15. [green-agent-age-of-inference-ii/src/utils/__init__.py](#green-agent-age-of-inference-ii-src-utils-__init__-py)
16. [green-agent-age-of-inference-ii/src/utils/call_llm.py](#green-agent-age-of-inference-ii-src-utils-call_llm-py)
17. [green-agent-age-of-inference-ii/src/utils/data_retrieval.py](#green-agent-age-of-inference-ii-src-utils-data_retrieval-py)
18. [green-agent-age-of-inference-ii/src/utils/gdsc_utils.py](#green-agent-age-of-inference-ii-src-utils-gdsc_utils-py)
19. [green-agent-age-of-inference-ii/src/utils/matching_rules.py](#green-agent-age-of-inference-ii-src-utils-matching_rules-py)
20. [green-agent-age-of-inference-ii/src/utils/s3_helper.py](#green-agent-age-of-inference-ii-src-utils-s3_helper-py)
21. [green-agent-age-of-inference-ii/tests/__init__.py](#green-agent-age-of-inference-ii-tests-__init__-py)
22. [green-agent-age-of-inference-ii/tests/test_call_llm.py](#green-agent-age-of-inference-ii-tests-test_call_llm-py)
23. [green-agent-age-of-inference-ii/tests/test_data_retrieval.py](#green-agent-age-of-inference-ii-tests-test_data_retrieval-py)
24. [green-agent-age-of-inference-ii/tests/test_integration.py](#green-agent-age-of-inference-ii-tests-test_integration-py)
25. [green-agent-age-of-inference-ii/tests/test_matching.py](#green-agent-age-of-inference-ii-tests-test_matching-py)
26. [green-agent-age-of-inference-ii/tests/test_matching_rules.py](#green-agent-age-of-inference-ii-tests-test_matching_rules-py)
27. [green-agent-age-of-inference-ii/tests/test_nodes.py](#green-agent-age-of-inference-ii-tests-test_nodes-py)
28. [green-agent-age-of-inference-ii/tests/test_utils.py](#green-agent-age-of-inference-ii-tests-test_utils-py)

---

## 📄 Source Files

### <a name="green-agent-age-of-inference-ii-analyze_parsed_data-py"></a>green-agent-age-of-inference-ii/analyze_parsed_data.py

> 💬 **Developer Note:** Our latest weapon.

**Size:** 3474 bytes

```python
import json
from pathlib import Path
from collections import Counter
import pandas as pd

# This script assumes it is run from the project's root directory.
PROFILES_DIR = Path("data/profiles")
PARSED_JOBS_FILE = Path("data/parsed_jobs.json")
PARSED_TRAININGS_FILE = Path("data/parsed_trainings.json")

def analyze_persona_profiles():
    """Analyzes the distribution of attributes across all persona profiles."""
    print("\n--- 📊 Analyzing Persona Profiles ---")
    
    if not PROFILES_DIR.exists():
        print(f"❌ ERROR: Profiles directory not found at '{PROFILES_DIR}'")
        return

    all_profiles = []
    for profile_file in PROFILES_DIR.glob("*.json"):
        with open(profile_file, 'r') as f:
            all_profiles.append(json.load(f))
            
    if not all_profiles:
        print("No persona profiles found to analyze.")
        return

    df = pd.DataFrame(all_profiles)
    
    print(f"\nTotal Personas Analyzed: {len(df)}")

    # 1. Education Level Distribution
    print("\n🎓 Education Level Distribution:")
    edu_counts = df['education_level'].value_counts().sort_index()
    print(edu_counts.to_string())

    # 2. Experience Distribution
    print("\n📈 Years of Experience Distribution:")
    exp_counts = df['experience_years'].value_counts().sort_index()
    print(exp_counts.to_string())
    print(f"  - Average Experience: {df['experience_years'].mean():.2f} years")
    print(f"  - Median Experience: {df['experience_years'].median():.2f} years")

    # 3. Location Distribution
    print("\n📍 Location Distribution (Top 5):")
    loc_counts = df['city'].value_counts()
    print(loc_counts.head(5).to_string())


def analyze_parsed_file(file_path: Path, item_type: str):
    """Generic analyzer for parsed jobs or trainings JSON files."""
    print(f"\n--- 📊 Analyzing Parsed {item_type.capitalize()} Data ---")
    
    if not file_path.exists():
        print(f"❌ ERROR: Parsed data file not found at '{file_path}'")
        return
        
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    print(f"\nTotal {item_type.capitalize()} Analyzed: {len(df)}")
    
    if item_type == "jobs":
        # 1. Education Requirements
        print("\n🎓 Required Education Level Distribution:")
        edu_counts = df['education_level'].fillna('Not Specified').value_counts().sort_index()
        print(edu_counts.to_string())

        # 2. Experience Requirements
        print("\n📈 Required Years of Experience Distribution:")
        exp_counts = df['experience_years'].value_counts().sort_index()
        print(exp_counts.to_string())

        # 3. Location Distribution
        print("\n📍 Location Distribution (Top 5):")
        loc_counts = df['city'].fillna('Not Specified').value_counts()
        print(loc_counts.head(5).to_string())
        print(f"  - Remote Jobs: {df['is_remote'].sum()}")

    elif item_type == "trainings":
        # 1. Training Prerequisites
        print("\n🎓 Required Prerequisite Level Distribution:")
        req_counts = df['required_level'].fillna('Not Specified').value_counts().sort_index()
        print(req_counts.to_string())


if __name__ == "__main__":
    print("--- 🔬 Kicking off Data-Driven Filter Analysis ---")
    analyze_persona_profiles()
    analyze_parsed_file(PARSED_JOBS_FILE, "jobs")
    analyze_parsed_file(PARSED_TRAININGS_FILE, "trainings")
    print("\n--- ✅ Analysis Complete ---")
```

---

### <a name="green-agent-age-of-inference-ii-collect_python_codebase_info-py"></a>green-agent-age-of-inference-ii/collect_python_codebase_info.py

> 💬 **Developer Note:** n

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-collect_python_codebase_info_v2-py"></a>green-agent-age-of-inference-ii/collect_python_codebase_info_v2.py

> 💬 **Developer Note:** The script that was used to create this documentation.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-conduct_interviews-py"></a>green-agent-age-of-inference-ii/conduct_interviews.py

> 💬 **Developer Note:** The script that conducted interviews and generate parsed data for personas.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-conduct_interviews_old-py"></a>green-agent-age-of-inference-ii/conduct_interviews_old.py

> 💬 **Developer Note:** legacy version

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-generate_recommendations-py"></a>green-agent-age-of-inference-ii/generate_recommendations.py

> 💬 **Developer Note:** The main script.

**Size:** 5142 bytes

```python
# generate_recommendations.py
import logging
import time
import argparse
import json
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from src.flow import create_recommendation_flow # Renamed from create_main_flow
from src.nodes import PersonaProfile, JobProfile, TrainingProfile
from src.utils.call_llm import COST_TRACKER

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_for_persona(flow, persona_profile: PersonaProfile, parsed_data: dict) -> dict:
    """Runs the recommendation part of the flow for a single, pre-interviewed persona."""
    logger.info(f"--- Generating recommendation for: {persona_profile.persona_id} ---")
    
    shared = {
        "persona_id": persona_profile.persona_id,
        "persona_profile": persona_profile,
        "parsed_jobs": parsed_data["parsed_jobs"],
        "parsed_trainings": parsed_data["parsed_trainings"]
    }
    
    # The flow now starts with the DecisionNode
    flow.run(shared)
    return shared

def main():
    parser = argparse.ArgumentParser(description="Generate recommendations for pre-interviewed persona profiles.")
    parser.add_argument('--personas', type=str, help='Optional: A range of persona IDs to process, e.g., "1-10". Processes all found profiles if not specified.')
    args = parser.parse_args()

    # --- Load Static Data ---
    try:
        with open("data/parsed_jobs.json", 'r') as f:
            parsed_jobs_data = [JobProfile.model_validate(j) for j in json.load(f)]
        with open("data/parsed_trainings.json", 'r') as f:
            parsed_trainings_data = [TrainingProfile.model_validate(t) for t in json.load(f)]
        parsed_data = {"parsed_jobs": parsed_jobs_data, "parsed_trainings": parsed_trainings_data}
    except FileNotFoundError as e:
        logger.error(f"Could not load parsed data. Please run 'parse_data.py' first. Error: {e}")
        return

    # --- Load Persona Profiles ---
    profiles_dir = Path("data/profiles")
    if not profiles_dir.exists():
        logger.error(f"Profiles directory not found at '{profiles_dir}'. Please run 'conduct_interviews.py' first.")
        return
        
    all_profile_files = sorted(profiles_dir.glob("persona_*.json"))
    
    # Filter profiles based on --personas argument if provided
    profiles_to_process = []
    if args.personas:
        start_id, end_id = map(int, args.personas.split('-'))
        requested_ids = {f"persona_{i:03d}" for i in range(start_id, end_id + 1)}
        for pf in all_profile_files:
            if pf.stem in requested_ids:
                profiles_to_process.append(pf)
    else:
        profiles_to_process = all_profile_files

    if not profiles_to_process:
        logger.error("No persona profiles found to process for the given range.")
        return

    # --- Run Recommendation Flow ---
    rec_flow = create_recommendation_flow()
    all_recommendations = []
    run_start_time = time.time()

    logger.info(f"--- 🧠 Starting recommendation generation for {len(profiles_to_process)} personas ---")

    for profile_file in tqdm(profiles_to_process, desc="Generating Recommendations"):
        try:
            with open(profile_file, 'r') as f:
                # Add persona_id to the profile data before validation
                profile_data = json.load(f)
                profile_data['persona_id'] = profile_file.stem
                persona_profile = PersonaProfile.model_validate(profile_data)
            
            final_shared = run_for_persona(rec_flow, persona_profile, parsed_data)
            if "final_recommendation" in final_shared:
                all_recommendations.append(final_shared["final_recommendation"])
        except Exception as e:
            logger.error(f"Error generating recommendation for {profile_file.stem}: {e}", exc_info=True)
            all_recommendations.append({"persona_id": profile_file.stem, "predicted_type": "awareness", "predicted_items": "error"})

    run_end_time = time.time()
    
    # --- Save Submission File and Report Metrics ---
    submission_path = Path("output") / "submission.json"
    submission_path.parent.mkdir(exist_ok=True)
    with open(submission_path, 'w') as f:
        json.dump(all_recommendations, f, indent=2, ensure_ascii=False)

    logger.info("\n--- ✅ Recommendation Generation Complete ---")
    logger.info(f"Total execution time: {run_end_time - run_start_time:.2f} seconds.")
    logger.info(f"Average time per persona: {(run_end_time - run_start_time) / len(profiles_to_process):.2f} seconds.")
    logger.info(f"Submission file for {len(all_recommendations)} personas saved to {submission_path}")
    
    logger.info("\n--- 📊 Cost & Token Usage for Recommendations ---")
    logger.info(f"Estimated Total Cost: ${COST_TRACKER['total_cost']:.4f}")
    if COST_TRACKER['by_model']:
        for model, data in COST_TRACKER['by_model'].items():
            logger.info(f"  - Model: {model}, Cost: ${data['cost']:.4f}, Calls: {data['calls']}")

if __name__ == "__main__":
    main()
```

---

### <a name="green-agent-age-of-inference-ii-generic_s3_downloader-py"></a>green-agent-age-of-inference-ii/generic_s3_downloader.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-main-py"></a>green-agent-age-of-inference-ii/main.py

> 💬 **Developer Note:** legacy main file

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-parse_data-py"></a>green-agent-age-of-inference-ii/parse_data.py

> 💬 **Developer Note:** This script was used to parse the job and training markdown files

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-pocketflow-__init__-py"></a>green-agent-age-of-inference-ii/pocketflow/__init__.py

> 💬 **Developer Note:** The main framework.

**Size:** 5211 bytes

```python
import asyncio, warnings, copy, time

class BaseNode:
    def __init__(self): self.params,self.successors={},{}
    def set_params(self,params): self.params=params
    def next(self,node,action="default"):
        if action in self.successors: warnings.warn(f"Overwriting successor for action '{action}'")
        self.successors[action]=node; return node
    def prep(self,shared): pass
    def exec(self,prep_res): pass
    def post(self,shared,prep_res,exec_res): pass
    def _exec(self,prep_res): return self.exec(prep_res)
    def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
    def run(self,shared): 
        if self.successors: warnings.warn("Node won't run successors. Use Flow.")  
        return self._run(shared)
    def __rshift__(self,other): return self.next(other)
    def __sub__(self,action):
        if isinstance(action,str): return _ConditionalTransition(self,action)
        raise TypeError("Action must be a string")

class _ConditionalTransition:
    def __init__(self,src,action): self.src,self.action=src,action
    def __rshift__(self,tgt): return self.src.next(tgt,self.action)

class Node(BaseNode):
    def __init__(self,max_retries=1,wait=0): super().__init__(); self.max_retries,self.wait=max_retries,wait
    def exec_fallback(self,prep_res,exc): raise exc
    def _exec(self,prep_res):
        for self.cur_retry in range(self.max_retries):
            try: return self.exec(prep_res)
            except Exception as e:
                if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
                if self.wait>0: time.sleep(self.wait)

class BatchNode(Node):
    def _exec(self,items): return [super(BatchNode,self)._exec(i) for i in (items or [])]

class Flow(BaseNode):
    def __init__(self,start=None): super().__init__(); self.start_node=start
    def start(self,start): self.start_node=start; return start
    def get_next_node(self,curr,action):
        nxt=curr.successors.get(action or "default")
        if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
        return nxt
    def _orch(self,shared,params=None):
        curr,p,last_action =copy.copy(self.start_node),(params or {**self.params}),None
        while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
        return last_action
    def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
    def post(self,shared,prep_res,exec_res): return exec_res

class BatchFlow(Flow):
    def _run(self,shared):
        pr=self.prep(shared) or []
        for bp in pr: self._orch(shared,{**self.params,**bp})
        return self.post(shared,pr,None)

class AsyncNode(Node):
    async def prep_async(self,shared): pass
    async def exec_async(self,prep_res): pass
    async def exec_fallback_async(self,prep_res,exc): raise exc
    async def post_async(self,shared,prep_res,exec_res): pass
    async def _exec(self,prep_res): 
        for self.cur_retry in range(self.max_retries):
            try: return await self.exec_async(prep_res)
            except Exception as e:
                if self.cur_retry==self.max_retries-1: return await self.exec_fallback_async(prep_res,e)
                if self.wait>0: await asyncio.sleep(self.wait)
    async def run_async(self,shared): 
        if self.successors: warnings.warn("Node won't run successors. Use AsyncFlow.")  
        return await self._run_async(shared)
    async def _run_async(self,shared): p=await self.prep_async(shared); e=await self._exec(p); return await self.post_async(shared,p,e)
    def _run(self,shared): raise RuntimeError("Use run_async.")

class AsyncBatchNode(AsyncNode,BatchNode):
    async def _exec(self,items): return [await super(AsyncBatchNode,self)._exec(i) for i in items]

class AsyncParallelBatchNode(AsyncNode,BatchNode):
    async def _exec(self,items): return await asyncio.gather(*(super(AsyncParallelBatchNode,self)._exec(i) for i in items))

class AsyncFlow(Flow,AsyncNode):
    async def _orch_async(self,shared,params=None):
        curr,p,last_action =copy.copy(self.start_node),(params or {**self.params}),None
        while curr: curr.set_params(p); last_action=await curr._run_async(shared) if isinstance(curr,AsyncNode) else curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
        return last_action
    async def _run_async(self,shared): p=await self.prep_async(shared); o=await self._orch_async(shared); return await self.post_async(shared,p,o)
    async def post_async(self,shared,prep_res,exec_res): return exec_res

class AsyncBatchFlow(AsyncFlow,BatchFlow):
    async def _run_async(self,shared):
        pr=await self.prep_async(shared) or []
        for bp in pr: await self._orch_async(shared,{**self.params,**bp})
        return await self.post_async(shared,pr,None)

class AsyncParallelBatchFlow(AsyncFlow,BatchFlow):
    async def _run_async(self,shared): 
        pr=await self.prep_async(shared) or []
        await asyncio.gather(*(self._orch_async(shared,{**self.params,**bp}) for bp in pr))
        return await self.post_async(shared,pr,None)
```

---

### <a name="green-agent-age-of-inference-ii-src-__init__-py"></a>green-agent-age-of-inference-ii/src/__init__.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-flow-py"></a>green-agent-age-of-inference-ii/src/flow.py

> 💬 **Developer Note:** The workflow.

**Size:** 1656 bytes

```python
# src/flow.py
import logging
from pocketflow import Flow
from src.nodes import (
    DecisionNode,
    ProvideAwarenessNode,
    FindTrainingsOnlyNode,
    FindJobsAndTrainingsNode,
    FinalizeOutputNode,
    # No longer need ExtractProfileNode here
)

logger = logging.getLogger(__name__)
# (logging setup remains the same)

def create_recommendation_flow() -> Flow:
    """
    Assembles the workflow that starts AFTER a persona profile is already known.
    """
    logger.info("Creating the recommendation-only flow...")

    # Instantiate nodes
    decision_node = DecisionNode()
    provide_awareness_node = ProvideAwarenessNode()
    find_trainings_only_node = FindTrainingsOnlyNode()
    find_jobs_and_trainings_node = FindJobsAndTrainingsNode()
    finalize_output_node = FinalizeOutputNode()

    # Configure the jobs node for high-quality scoring
    find_jobs_and_trainings_node.set_params({
        "use_cache_for_scoring": True,
        "scoring_model": "mistral-large-latest"
    })
    
    # Connect nodes
    (decision_node - "provide_awareness_young") >> provide_awareness_node
    (decision_node - "provide_awareness_info") >> provide_awareness_node
    (decision_node - "recommend_trainings") >> find_trainings_only_node
    (decision_node - "recommend_jobs") >> find_jobs_and_trainings_node

    provide_awareness_node >> finalize_output_node
    find_trainings_only_node >> finalize_output_node
    find_jobs_and_trainings_node >> finalize_output_node

    # The flow now starts with the DecisionNode
    rec_flow = Flow(start=decision_node)
    
    logger.info("Recommendation-only flow created successfully.")
    return rec_flow
```

---

### <a name="green-agent-age-of-inference-ii-src-flow_old-py"></a>green-agent-age-of-inference-ii/src/flow_old.py

> 💬 **Developer Note:** legacy

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-nodes-py"></a>green-agent-age-of-inference-ii/src/nodes.py

> 💬 **Developer Note:** The most important file.

**Size:** 34120 bytes

```python
import logging
import json
from pathlib import Path
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any
from tqdm import tqdm

from src.utils.data_retrieval import load_all_data
from src.utils.gdsc_utils import chat_with_persona, sanity_check
from src.utils.call_llm import call_llm
from src.utils.matching_rules import EDUCATION_LEVELS, apply_hard_filters, get_required_trainings

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Pydantic Data Models ---
class PersonaProfile(BaseModel):
    persona_id: str = Field(..., description="The persona's unique identifier.")
    age: int = Field(..., description="The persona's age in years.")
    city: Optional[str] = Field(None, description="The city where the job is located, if specified.")
    education_level: str = Field(..., description="The highest level of education achieved, e.g., 'Ensino Fundamental'.")
    experience_years: int = Field(..., description="Estimated years of professional experience.")
    skills: List[str] = Field(..., description="A list of key skills the persona mentioned.")
    goals: str = Field(..., description="A summary of the persona's career goals or immediate intentions.")
    is_open_to_relocate: bool = Field(..., description="Whether the persona is willing to relocate for a job.")
    languages: List[str] = Field(default=["Portuguese"], description="List of languages the persona speaks.")

class JobProfile(BaseModel):
    job_id: str = Field(..., description="The unique identifier for the job (e.g., 'j10').")
    title: str = Field(..., description="The job title.")
    city: Optional[str] = Field(None, description="The city where the job is located, if specified.")
    is_remote: bool = Field(default=False, description="Whether the job can be done remotely.")
    education_level: Optional[str] = Field(None, description="The minimum education level required.")
    experience_years: int = Field(default=0, description="The minimum years of experience required.")
    languages: List[str] = Field(default=[], description="List of required languages.")
    required_skills: List[str] = Field(default=[], description="List of essential skills for the job.")
    

class TrainingProfile(BaseModel):
    training_id: str = Field(..., description="The unique identifier for the training (e.g., 'tr15').")
    title: str = Field(..., description="The title of the training program.")
    offered_skills: List[str] = Field(default=[], description="A list of skills this training provides.")
    required_level: Optional[str] = Field(None, description="The prerequisite skill level or education, if any.")

# --- Nodes ---
class LoadStaticDataNode(Node):
    # (unchanged)
    def prep(self, shared):
        return None
    def exec(self, prep_res):
        logger.info("Loading all static data (jobs and trainings)...")
        jobs = load_all_data("jobs")
        trainings = load_all_data("trainings")
        return {"jobs": jobs, "trainings": trainings}
    def post(self, shared, prep_res, exec_res):
        shared["all_jobs"] = exec_res.get("jobs", [])
        shared["all_trainings"] = exec_res.get("trainings", [])
        logger.info(f"Loaded {len(shared['all_jobs'])} jobs and {len(shared['all_trainings'])} trainings into shared store.")

class ParseStaticDataNode(Node):
    """
    CORRECTED: Parses raw job and training markdown files into structured Pydantic objects.
    """
    # CORRECTED: The prep method now correctly fetches the raw data from the shared store.
    def prep(self, shared):
        return {
            "raw_jobs": shared.get("all_jobs", []),
            "raw_trainings": shared.get("all_trainings", [])
        }
        
    # def _get_cache_path(self, name: str) -> Path:
    #     return Path("data") / f"parsed_{name}.json"
    def _get_cache_path(self, name: str, suffix: str = "") -> Path:
        if suffix:
            return Path("data") / f"parsed_{name}{suffix}.json"
        return Path("data") / f"parsed_{name}.json"
        
    def _load_from_cache(self, name: str, model: BaseModel) -> Optional[List[BaseModel]]:
        # cache_path = self._get_cache_path(name)
        suffix = self.params.get("cache_suffix", "")
        cache_path = self._get_cache_path(name, suffix)
        if cache_path.exists():
            logger.info(f"Loading parsed {name} from cache: {cache_path}")
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [model.model_validate(item) for item in data]
        return None

    def _save_to_cache(self, name: str, data: List[BaseModel]):
        # cache_path = self._get_cache_path(name)
        suffix = self.params.get("cache_suffix", "")
        cache_path = self._get_cache_path(name, suffix)
        logger.info(f"Saving {len(data)} parsed {name} to cache: {cache_path}")
        dict_data = [item.model_dump() for item in data]
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, indent=2, ensure_ascii=False)

    def _parse_item(self, item: Dict[str, str], schema: Dict, item_id_key: str) -> Optional[Dict[str, Any]]:
        item_id = item.get("id")
        content = item.get("content")
        
        valid_levels = list(EDUCATION_LEVELS.keys())
        
        prompt = f"""
        Analyze the following document and extract its properties into a valid JSON object that strictly follows this schema.

        **CRITICAL INSTRUCTIONS:**
        1.  The '{item_id_key}' field MUST be set to the exact value '{item_id}'.
        2.  For the 'education_level' or 'required_level' field, you MUST map any prerequisite text to one of the **exact** string values from this list: `{valid_levels}`.
        3.  **You must infer the closest formal level.** For example:
            - If a job requires a "Tecnólogo degree", you must output "Tecnólogo".
            - If a training requires "basic experience with software", infer the most likely entry level, such as "Ensino Médio".
            - If the text explicitly states "None", "Nenhum", or there are truly no prerequisites, you MUST use `null`.

        JSON Schema:
        ---
        {json.dumps(schema, indent=2)}
        ---
        Document:
        ---
        {content}
        ---
        Respond ONLY with the JSON object.
        """
        try:
            parsing_model = self.params.get("parsing_model", "mistral-large-latest") # Default to large
            response_str = call_llm(prompt=prompt, use_cache=True, model=parsing_model)
            cleaned_str = response_str.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_str)
        except (json.JSONDecodeError, Exception) as e:
            logger.error(f"Failed to parse item {item_id}: {e}")
            return None

    # CORRECTED: The exec method now receives the raw data from prep_res.
    def exec(self, prep_res: Dict):
        raw_jobs = prep_res["raw_jobs"]
        raw_trainings = prep_res["raw_trainings"]
        
        parsed_jobs = self._load_from_cache("jobs", JobProfile)
        if not parsed_jobs:
            logger.info("Job cache not found. Parsing all jobs from markdown...")
            job_schema = JobProfile.model_json_schema()
            parsed_job_data = [
                self._parse_item(job, job_schema, "job_id") 
                for job in tqdm(raw_jobs, desc="Parsing Jobs")
            ]
            parsed_jobs = [JobProfile.model_validate(data) for data in parsed_job_data if data]
            self._save_to_cache("jobs", parsed_jobs)

        parsed_trainings = self._load_from_cache("trainings", TrainingProfile)
        if not parsed_trainings:
            logger.info("Training cache not found. Parsing all trainings from markdown...")
            training_schema = TrainingProfile.model_json_schema()
            parsed_training_data = [
                self._parse_item(training, training_schema, "training_id") 
                for training in tqdm(raw_trainings, desc="Parsing Trainings")
            ]
            parsed_trainings = [TrainingProfile.model_validate(data) for data in parsed_training_data if data]
            self._save_to_cache("trainings", parsed_trainings)
            
        return {"parsed_jobs": parsed_jobs, "parsed_trainings": parsed_trainings}
        
    def post(self, shared, prep_res, exec_res):
        # (unchanged)
        shared["parsed_jobs"] = exec_res.get("parsed_jobs", [])
        shared["parsed_trainings"] = exec_res.get("parsed_trainings", [])
        logger.info(f"Loaded {len(shared['parsed_jobs'])} parsed jobs and {len(shared['parsed_trainings'])} parsed trainings into shared store.")

class ExtractProfileNode(Node):
    def prep(self, shared):
        persona_id = shared.get("persona_id")
        if not persona_id:
            raise ValueError("persona_id not found in shared store.")
        return {"persona_id": persona_id}

    def exec(self, prep_res):
        persona_id = prep_res["persona_id"]
        
        # Get the model from params, defaulting to small for safety/testing
        interview_model = self.params.get("interview_model", "mistral-small-latest")
        logger.info(f"Starting DYNAMIC conversation with {persona_id} using model {interview_model}...")

        conversation_id = None
        conversation_history = []
        persona_profile = {}
        
        # --- Conversation Loop Constants ---
        MAX_TURNS = 8
        MIN_TURNS = 5

        for turn in range(MAX_TURNS):
            logger.info(f"Conversation Turn {turn + 1}/{MAX_TURNS}")
            
            # 1. Analyze current history...
            schema = PersonaProfile.model_json_schema()
            transcript = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in conversation_history])
            
            current_profile_data = {}
            if transcript:
                analysis_prompt = f"""
                Analyze the conversation transcript and extract the user's profile into a valid JSON object that strictly follows this schema.
                The 'persona_id' must be set to '{persona_id}'.
                If a value is not mentioned, omit the key.

                JSON Schema:
                ---
                {json.dumps(schema, indent=2)}
                ---
                Conversation Transcript:
                ---
                {transcript}
                ---
                Respond ONLY with the JSON object.
                """
                # Use the configured model for analysis
                profile_str = call_llm(prompt=analysis_prompt, use_cache=False, model=interview_model)
                try:
                    cleaned_str = profile_str.strip().replace("```json", "").replace("```", "")
                    current_profile_data = json.loads(cleaned_str)
                except (json.JSONDecodeError, Exception) as e:
                    logger.warning(f"Could not parse partial profile on turn {turn+1}: {e}. Continuing conversation.")

            is_complete = False
            missing_fields = []
            try:
                # Add persona_id to the data before validating
                if 'persona_id' not in current_profile_data:
                    current_profile_data['persona_id'] = persona_id
                PersonaProfile.model_validate(current_profile_data)
                is_complete = True
            except ValidationError as e:
                missing_fields = [err['loc'][0] for err in e.errors() if err['loc'][0] != 'persona_id']

            if is_complete and (turn + 1) >= MIN_TURNS:
                logger.info(f"Profile is complete after {turn + 1} turns. Ending conversation.")
                persona_profile = current_profile_data
                break
            else:
                 logger.info(f"Profile is not yet complete. Missing fields: {missing_fields if not is_complete else 'N/A (min turns not met)'}")

            # 3. Generate the next question
            if turn == 0:
                next_question = "Hello! To help you find the right green job opportunities, could you please tell me a bit about yourself? For example, your age, languages and current city in Brazil."
            else:
                next_question_prompt = f"""
                You are an expert career advisor conducting a friendly interview. Based on the conversation so far, you need to ask a question to gather the following missing information: {', '.join(missing_fields)}.
                
                - Ask only ONE clear and concise question.
                - Phrase the question naturally based on the last answer.
                - Do not repeat questions that have already been answered.

                Conversation History:
                ---
                {transcript}
                ---

                What is the next best question to ask? Respond ONLY with the question text.
                """
                # Use the configured model for generating questions
                next_question = call_llm(prompt=next_question_prompt, use_cache=False, model=interview_model)

            # 4. Interact with the persona
            logger.info(f"Asking: {next_question}")
            response_tuple = chat_with_persona(
                persona_id=persona_id, message=next_question, conversation_id=conversation_id
            )
            if response_tuple is None:
                raise RuntimeError("The chat_with_persona API call failed.")
            response, conversation_id = response_tuple
            logger.info(f"Response: {response}")
            conversation_history.append({"question": next_question, "answer": response})

            if turn == MAX_TURNS - 1:
                logger.warning(f"Max conversation turns ({MAX_TURNS}) reached. Proceeding with collected data.")
                persona_profile = current_profile_data

        # --- Final Validation ---
        try:
            final_profile = PersonaProfile.model_validate(persona_profile)
        except ValidationError as e:
            logger.error(f"Conversation ended, but profile is still incomplete. Raw data: {persona_profile}")
            raise RuntimeError(f"Could not build a complete persona profile. Validation errors: {e}")

        return {
            "persona_profile": final_profile,
            "conversation_id": conversation_id,
            "conversation_history": conversation_history
        }
    
    def post(self, shared, prep_res, exec_res):
        shared["persona_profile"] = exec_res["persona_profile"]
        shared["conversation_id"] = exec_res["conversation_id"]
        shared["conversation_history"] = exec_res["conversation_history"]
        logger.info(f"Successfully extracted and validated profile for {shared['persona_id']}.")
        
class DecisionNode(Node):
    def prep(self, shared):
        profile = shared.get("persona_profile")
        if not profile or not isinstance(profile, PersonaProfile):
            raise ValueError("A valid PersonaProfile object was not found in the shared store.")
        return profile
    def exec(self, profile: PersonaProfile) -> str:
        logger.info(f"Making decision for persona with age {profile.age} and goals: '{profile.goals}'")
        if profile.age < 16:
            logger.info("Decision: provide_awareness_young (age < 16)")
            return "provide_awareness_young"
        informational_keywords = ["exploring", "explorar", "curious", "curioso", "just looking", "só olhando", "not sure", "não sei"]
        if any(keyword in profile.goals.lower() for keyword in informational_keywords):
            logger.info("Decision: provide_awareness_info (informational goals)")
            return "provide_awareness_info"
        training_keywords = ["training", "treinamento", "courses", "cursos", "learn", "aprender", "study", "estudar", "upskill"]
        job_keywords = ["job", "emprego", "work", "trabalhar", "career", "carreira"]
        has_training_goal = any(keyword in profile.goals.lower() for keyword in training_keywords)
        has_job_goal = any(keyword in profile.goals.lower() for keyword in job_keywords)
        if has_training_goal and not has_job_goal:
            logger.info("Decision: recommend_trainings (training-focused goals)")
            return "recommend_trainings"
        logger.info("Decision: recommend_jobs (default path)")
        return "recommend_jobs"
    def post(self, shared, prep_res, exec_res: str) -> Optional[str]:
        shared["decision_action"] = exec_res
        logger.info(f"Decision action '{exec_res}' stored in shared store.")
        
        return exec_res
        
class ProvideAwarenessNode(Node):
    def prep(self, shared):
        decision = shared.get("decision_action")
        if not decision or "provide_awareness" not in decision:
            raise ValueError(f"Invalid decision action '{decision}' for ProvideAwarenessNode.")
        return decision
    def exec(self, decision: str) -> Dict[str, Any]:
        if decision == "provide_awareness_young":
            reason = "too_young"
            logger.info("Formatting awareness response for reason: too_young.")
        else:
            reason = "info"
            logger.info("Formatting awareness response for reason: info.")
        return {
            "predicted_type": "awareness",
            "predicted_items": reason
        }
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info(f"Awareness recommendation stored in 'intermediate_recommendations'.")

class FindTrainingsOnlyNode(Node):
    """
    Finds and recommends trainings by scoring all ELIGIBLE trainings for relevance.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        trainings = shared.get("parsed_trainings")
        if not profile or not trainings:
            raise ValueError("Persona profile or parsed trainings not found in shared store.")
        return {"profile": profile, "trainings": trainings}

    def _get_training_relevance_score(self, persona: PersonaProfile, training: TrainingProfile) -> int:
        """Calls a small LLM to score the relevance of a training to a persona's goals."""
        prompt = f"""
        On a scale of 1-10, how relevant is this training program to a person with the specific goal: "{persona.goals}"?

        Training Program:
        - Title: "{training.title}"
        - Skills Offered: {training.offered_skills}

        Focus only on the alignment with the person's stated goal.
        Respond ONLY with a valid JSON object like {{"score": N}}.
        """
        try:
            response_str = call_llm(prompt, model="mistral-small-latest", use_cache=True)
            cleaned_str = response_str.strip().replace("```json", "").replace("```", "")
            response_json = json.loads(cleaned_str)
            score = int(response_json.get("score", 0))
            logger.debug(f"Training {training.training_id} scored {score}.")
            return score
        except (json.JSONDecodeError, ValueError, Exception) as e:
            logger.warning(f"Could not parse relevance score for training {training.training_id}: {e}")
            return 0

    def _is_training_relevant_domain(self, persona_goals: str, training: TrainingProfile) -> bool:
        """
        Uses a cheap LLM call to quickly classify if a training is in a relevant domain.
        Returns True for "yes", False otherwise.
        """
        prompt = f"""
        A person has this career goal: "{persona_goals}"

        A training program is titled: "{training.title}" and offers these skills: {training.offered_skills}.

        Is this training program directly related to the person's stated career goal?
        
        Respond ONLY with the single word "yes" or "no".
        """
        try:
            # Use a fast, cheap model for this simple classification.
            response = call_llm(prompt, model="mistral-small-latest", use_cache=True)
            return response.strip().lower() == "yes"
        except Exception as e:
            logger.warning(f"Domain relevance check failed for training {training.training_id}: {e}")
            return False

    # def exec(self, prep_res: Dict) -> Dict[str, Any]:
    #     profile: PersonaProfile = prep_res["profile"]
    #     all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
    #     persona_edu_level_str = profile.education_level
    #     persona_edu_level_num = EDUCATION_LEVELS.get(persona_edu_level_str, 0)
        
    #     # --- START: DIAGNOSTIC LOGGING ---
    #     logger.info(f"DEBUG: Persona education level is '{persona_edu_level_str}' which maps to numeric value {persona_edu_level_num}.")
    #     # --- END: DIAGNOSTIC LOGGING ---

    #     candidate_trainings = []
    #     # --- ADDED A COUNTER FOR THE LOOP DIAGNOSTICS ---
    #     for i, training in enumerate(all_trainings):
    #         training_req_level_str = training.required_level
    #         training_req_level_num = EDUCATION_LEVELS.get(training_req_level_str, 0)
            
    #         # --- THIS IS THE CORRECT, STRICT LOGIC ---
    #         is_next_level = (training_req_level_num == persona_edu_level_num + 1)
    #         is_open_to_all = (training_req_level_num == 0)

    #         if is_next_level or is_open_to_all:
    #             candidate_trainings.append(training)
            
    #         # --- START: DIAGNOSTIC LOGGING FOR THE FIRST 5 ITEMS ---
    #         if i < 5:
    #             logger.info(
    #                 f"DEBUG LOOP {i}: "
    #                 f"Training '{training.training_id}' (req: '{training_req_level_str}' -> {training_req_level_num}). "
    #                 f"Condition check: is_next_level ({is_next_level}) or is_open_to_all ({is_open_to_all}). "
    #                 f"Result: {'ADDED' if is_next_level or is_open_to_all else 'SKIPPED'}"
    #             )
    #         # --- END: DIAGNOSTIC LOGGING ---

    #     logger.info(f"Found {len(candidate_trainings)} candidate trainings after a STRICT eligibility filter.")
        
    #     if not candidate_trainings:
    #         return {"predicted_type": "trainings_only", "trainings": []}

    #     # The rest of the function remains the same...
    #     scored_trainings = []
    #     for training in tqdm(candidate_trainings, desc="Scoring eligible trainings", disable=len(candidate_trainings) < 5):
    #         score = self._get_training_relevance_score(profile, training)
    #         scored_trainings.append({"training": training, "score": score})
            
    #     sorted_trainings = sorted(scored_trainings, key=lambda x: x["score"], reverse=True)
    #     top_trainings = [item["training"] for item in sorted_trainings[:5]] 
        
    #     recommended_trainings = [{"training_id": t.training_id} for t in top_trainings]
    #     logger.info(f"Recommending top {len(recommended_trainings)} most relevant trainings.")

    #     return {
    #         "predicted_type": "trainings_only",
    #         "trainings": recommended_trainings
    #     }          
    
    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
        persona_edu_level_str = profile.education_level
        persona_edu_level_num = EDUCATION_LEVELS.get(persona_edu_level_str, 0)

        # --- STAGE 1: Eligibility Filter (Fast, Rule-Based) ---
        eligible_trainings = []
        for training in all_trainings:
            training_req_level_str = training.required_level
            training_req_level_num = EDUCATION_LEVELS.get(training_req_level_str, 0)
            
            is_next_level = (training_req_level_num == persona_edu_level_num + 1)
            is_open_to_all = (training_req_level_num == 0)

            if is_next_level or is_open_to_all:
                eligible_trainings.append(training)
        
        logger.info(f"Found {len(eligible_trainings)} trainings that are educationally eligible.")
        if not eligible_trainings:
            return {"predicted_type": "trainings_only", "trainings": []}

        # --- STAGE 2: Domain Relevance Filter (Cheap LLM Classification) ---
        domain_relevant_trainings = [
            t for t in tqdm(eligible_trainings, desc="Filtering trainings by domain")
            if self._is_training_relevant_domain(profile.goals, t)
        ]
        
        logger.info(f"Found {len(domain_relevant_trainings)} trainings that are domain-relevant.")
        if not domain_relevant_trainings:
            # Fallback: if the strict domain filter yields nothing, recommend the top 5 eligible trainings
            # This prevents returning an empty list if the classifier is too aggressive.
            top_eligible = eligible_trainings[:5]
            logger.warning("Domain filter found no trainings. Falling back to top 5 eligible trainings.")
            fallback_recs = [{"training_id": t.training_id} for t in top_eligible]
            return {"predicted_type": "trainings_only", "trainings": fallback_recs}
            
        # --- STAGE 3: Final Scoring (More Expensive LLM on a small list) ---
        scored_trainings = []
        for training in tqdm(domain_relevant_trainings, desc="Scoring final trainings for relevance"):
            score = self._get_training_relevance_score(profile, training)
            scored_trainings.append({"training": training, "score": score})
            
        sorted_trainings = sorted(scored_trainings, key=lambda x: x["score"], reverse=True)
        top_trainings = [item["training"] for item in sorted_trainings[:5]] 
        
        recommended_trainings = [{"training_id": t.training_id} for t in top_trainings]
        logger.info(f"Recommending top {len(recommended_trainings)} most relevant trainings after final scoring.")

        return {
            "predicted_type": "trainings_only",
            "trainings": recommended_trainings
        }
        
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info("Training-only recommendation stored in 'intermediate_recommendations'.")
        
class FindJobsAndTrainingsNode(Node):
    """
    Finds suitable jobs using a hybrid approach:
    1. Fast, rule-based hard filters to find all technically eligible jobs.
    2. An LLM-based "soft filter" to score the relevance of eligible jobs.
    3. Recommends trainings for skill gaps on only the top-scoring jobs.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        jobs = shared.get("parsed_jobs")
        trainings = shared.get("parsed_trainings")
        if not all([profile, jobs, trainings]):
            raise ValueError("Persona profile, parsed jobs, or parsed trainings not found.")
        return {"profile": profile, "jobs": jobs, "trainings": trainings}

    def _get_relevance_score(self, persona: PersonaProfile, job: JobProfile, use_cache: bool = True, model: str = "mistral-small-latest") -> int:
        """Calls an LLM to score the relevance of a job to a persona."""
        # --- NEW, MORE ROBUST PROMPT ---
        prompt = f"""
        You are an expert career advisor in Brazil. Your task is to score the relevance of a job for a specific persona based on their skills and, most importantly, their stated career goals.

        **Persona Profile:**
        - **Stated Goals:** "{persona.goals}"
        - **Existing Skills:** {persona.skills}

        **Job to Evaluate:**
        - **Title:** "{job.title}"
        - **Required Skills:** {job.required_skills}

        **Scoring Criteria:**
        - **High Score (8-10):** The job title and its domain (e.g., finance, data, sustainability) directly align with the persona's stated goals.
        - **Medium Score (4-7):** The job shares keywords (like 'Analyst') but is in a different domain than the persona's goals (e.g., Design Analyst for a Data Analyst persona).
        - **Low Score (1-3):** The job is in a completely different field.

        On a scale of 1 to 10, how relevant is this job to the persona?

        **CRITICAL INSTRUCTION:** Your response MUST be a single, valid JSON object and nothing else. The 'reasoning' string must NOT contain any newline characters (`\\n`) or other control characters. It must be a single line of text.

        **Example of a valid response:**
        {{"score": 8, "reasoning": "This job is a strong match because the domain aligns with the persona's goals."}}

        Respond now.
        """
        try:
            response_str = call_llm(prompt=prompt, use_cache=use_cache, model=model)
            # Standard cleaning should be sufficient with the improved prompt
            cleaned_str = response_str.strip().replace("```json", "").replace("```", "")
            response_json = json.loads(cleaned_str)
            score = int(response_json.get("score", 0))
            logger.debug(f"Job {job.job_id} ('{job.title}') scored {score} using {model}. Reason: {response_json.get('reasoning')}")
            return score
        except (json.JSONDecodeError, ValueError, Exception) as e:
            logger.warning(f"Could not parse relevance score for job {job.job_id} using {model}. Error: {e}. Raw response: '{response_str}'")
            return 0

    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_jobs: List[JobProfile] = prep_res["jobs"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]

        # Get parameters from the node instance
        use_cache_for_scoring = self.params.get("use_cache_for_scoring", True)
        scoring_model = self.params.get("scoring_model", "mistral-small-latest")
        logger.info(f"Using model '{scoring_model}' for relevance scoring.")

        profile_dict = profile.model_dump()

        # candidate_jobs = [
        #     job for job in all_jobs 
        #     if apply_hard_filters(profile_dict, job.model_dump())
        # ]
        candidate_jobs = []
        failure_reasons = {}
        for job in all_jobs:
            is_match, reason = apply_hard_filters(profile_dict, job.model_dump())
            if is_match:
                candidate_jobs.append(job)
            else:
                # Log the reason for the first few failures to avoid spamming the console
                if len(failure_reasons) < 5:
                    failure_reasons[reason] = failure_reasons.get(reason, 0) + 1
        
        # Log a summary of why jobs were filtered out
        if not candidate_jobs:
            logger.warning("Top 5 reasons for job filter failures:")
            for reason, count in failure_reasons.items():
                logger.warning(f"  - [{count} times] {reason}")
        logger.info(f"Found {len(candidate_jobs)} candidate jobs after applying hard filters.")

        if not candidate_jobs:
            return {"predicted_type": "jobs+trainings", "jobs": []}

        scored_jobs = []
        for job in tqdm(candidate_jobs, desc=f"Scoring jobs with {scoring_model}", disable=len(candidate_jobs) < 5):
            score = self._get_relevance_score(profile, job, use_cache=use_cache_for_scoring, model=scoring_model)
            scored_jobs.append({"job": job, "score": score})

        sorted_jobs = sorted(scored_jobs, key=lambda x: x["score"], reverse=True)
        
        top_jobs = [item["job"] for item in sorted_jobs[:3]]
        logger.info(f"Selected top {len(top_jobs)} jobs after relevance scoring.")

        job_recommendations = []
        for job in top_jobs:
            job_dict = job.model_dump()
            missing_skills = get_required_trainings(profile_dict, job_dict)
            
            suggested_trainings = []
            if missing_skills:
                for skill in missing_skills:
                    matching_trainings = [
                        {"training_id": t.training_id}
                        for t in all_trainings
                        if skill.lower() in [s.lower() for s in t.offered_skills]
                    ]
                    if matching_trainings:
                        suggested_trainings.append({
                            "missing_skill": skill,
                            "trainings": matching_trainings
                        })
            
            job_recommendations.append({
                "job_id": job.job_id,
                "suggested_trainings": suggested_trainings
            })

        return {
            "predicted_type": "jobs+trainings",
            "jobs": job_recommendations
        }
        
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info("Jobs+trainings recommendation stored in 'intermediate_recommendations'.")
        
class FinalizeOutputNode(Node):
    def prep(self, shared):
        persona_id = shared.get("persona_id")
        recs = shared.get("intermediate_recommendations")
        if not persona_id or not recs:
            raise ValueError("Persona ID or intermediate recommendations not found in shared store.")
        return {"persona_id": persona_id, "recommendations": recs}
    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        final_output = {
            "persona_id": prep_res["persona_id"],
            **prep_res["recommendations"]
        }
        logger.info(f"Final output formatted for persona {prep_res['persona_id']}.")
        return final_output
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["final_recommendation"] = exec_res
        logger.info("Final recommendation stored in shared store.")
```

---

### <a name="green-agent-age-of-inference-ii-src-utils-__init__-py"></a>green-agent-age-of-inference-ii/src/utils/__init__.py

**Size:** 0 bytes

```python

```

---

### <a name="green-agent-age-of-inference-ii-src-utils-call_llm-py"></a>green-agent-age-of-inference-ii/src/utils/call_llm.py

> 💬 **Developer Note:** LLM calling utility

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-utils-data_retrieval-py"></a>green-agent-age-of-inference-ii/src/utils/data_retrieval.py

**Size:** 2940 bytes

```python
import logging
from pathlib import Path
from typing import List, Dict, Literal

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def load_all_data(data_type: Literal["jobs", "trainings"]) -> List[Dict[str, str]]:
    """
    Loads all markdown files from the specified data directory.

    This function looks for the 'data' directory starting from the
    parent of the current script's location, making it robust to
    being called from different working directories (e.g., /src, /tests, /).

    Args:
        data_type: The type of data to load, either "jobs" or "trainings".

    Returns:
        A list of dictionaries, where each dictionary contains the 'id'
        (from the filename) and 'content' of a markdown file.
        Returns an empty list if the directory is not found.
    """
    # --- Robust Path Resolution ---
    # Assumes the script is in a subdirectory of the project root (e.g., src/utils)
    # and navigates up to find the 'data' directory.
    base_path = Path(__file__).resolve().parent.parent.parent
    data_dir = base_path / 'data' / data_type

    if not data_dir.exists():
        logger.error(f"Data directory not found at: {data_dir}")
        return []

    loaded_data = []
    files = sorted(data_dir.glob('*.md'))
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            item_id = file_path.stem  # .stem gets the filename without extension
            loaded_data.append({'id': item_id, 'content': content})
        except Exception as e:
            logger.warning(f"Could not read or process file {file_path}: {e}")
            
    logger.info(f"Successfully loaded {len(loaded_data)} items from '{data_dir}'")
    return loaded_data

if __name__ == '__main__':
    print("--- Running Self-Test for data_retrieval utility ---")
    
    jobs_data = load_all_data("jobs")
    if jobs_data:
        print(f"\nLoaded {len(jobs_data)} job postings.")
        print("Sample job item:")
        print(f"  ID: {jobs_data[0]['id']}")
        print(f"  Content snippet: {jobs_data[0]['content'][:100].strip()}...")
    else:
        print("\nCould not load job postings. Check directory path.")

    trainings_data = load_all_data("trainings")
    if trainings_data:
        print(f"\nLoaded {len(trainings_data)} training programs.")
        print("Sample training item:")
        print(f"  ID: {trainings_data[0]['id']}")
        print(f"  Content snippet: {trainings_data[0]['content'][:100].strip()}...")
    else:
        print("\nCould not load training programs. Check directory path.")
    
    print("\n--- Self-Test Complete ---")

```

---

### <a name="green-agent-age-of-inference-ii-src-utils-gdsc_utils-py"></a>green-agent-age-of-inference-ii/src/utils/gdsc_utils.py

> 💬 **Developer Note:** THE OFFICIAL UTILS FROM GDSC.

**Size:** 16361 bytes

```python
"""
Shared utilities for GDSC-8 challenge.

Pro tip: Keep notebooks for exploration, modules for production code.
This separation makes your code testable, reusable, and maintainable.
"""
import json
import boto3
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


def save_json(path: str | Path, data: Dict | List) -> None:
    """
    Save data to JSON file with proper error handling.

    Args:
        path: Output file path
        data: Data to save (dict or list)

    Example:
        >>> results = [{"persona_id": "p1", "predicted_type": "awareness"}]
        >>> save_json("submission.json", results)
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_json(path: str | Path) -> Dict | List:
    """
    Load JSON data from file.

    Args:
        path: Input file path

    Returns:
        Loaded JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def load_file_content(path: str | Path) -> str:
    """
    Load raw text content from a file.

    Args:
        path: Input file path

    Returns:
        File contents as string
    """
    path = Path(path)
    with path.open('r', encoding='utf-8') as file:
        return file.read()


def aws_signed_request(
    path: str,
    method: str,
    payload: Optional[Any] = None,
    verbose: bool = True,
) -> Optional[requests.Response | bool]:
    """Make a SigV4 signed request to the challenge API.

    Lean error handling: raises RuntimeError on failure.

    Args:
        path: API path segment (e.g. "chat", "submit", "health")
        method: HTTP verb (GET/POST)
        payload: dict / list / JSON-string / None
        verbose: print status messages

    Returns:
        Response object, True (for health success), or None/False on failure
    """
    base_url = "https://cygeoykm2i.execute-api.us-east-1.amazonaws.com/main"

    # Normalize payload into raw JSON string (boto3 signing sends raw body)
    body = None
    if payload is not None:
        try:
            if isinstance(payload, (dict, list)):
                body = json.dumps(payload)
            elif isinstance(payload, (str, bytes)):
                body = payload if isinstance(payload, str) else payload.decode('utf-8')
            else:  # Fallback attempt json serialization
                body = json.dumps(payload)
        except Exception as e:  # pragma: no cover
            msg = f"Failed to serialize payload for path '{path}'"
            if verbose:
                print(f"❌ {msg}\n   ↳ {e}")
            raise RuntimeError(msg) from e

    try:
        session = boto3.Session(region_name='us-east-1')
        credentials = session.get_credentials()
        if not credentials:
            msg = "AWS credentials not found (configure with aws configure)"
            if verbose:
                print(f"❌ {msg}")
            raise RuntimeError(msg)

        headers = {'Content-Type': 'application/json'}
        request = AWSRequest(url=f"{base_url}/{path}", method=method.upper(), data=body, headers=headers)
        SigV4Auth(credentials, 'execute-api', 'us-east-1').add_auth(request)

        try:
            response = requests.request(
                method=str(request.method),
                url=str(request.url),
                headers=dict(request.headers),
                data=request.body,
            )
        except requests.RequestException as e:
            msg = f"Network error during request to '{path}'"
            if verbose:
                print(f"❌ {msg}\n   ↳ {e}")
            raise RuntimeError(msg) from e

        if response.status_code == 200:
            if verbose:
                print("✅ API request successful")
            return response if path != "health" else True

        # Non-200 status handling
        msg = f"API call '{path}' failed: status={response.status_code} body={response.text[:300]}"
        if verbose:
            print(f"❌ {msg}")
        raise RuntimeError(msg)

    except Exception as e:  # pragma: no cover - broad fallback
        msg = f"Unexpected error during signed request to '{path}'"
        if verbose:
            print(f"❌ {msg}\n   ↳ {e}")
        raise RuntimeError(msg) from e


def sanity_check(verbose: bool = True) -> bool:
    """Quick connectivity & credentials check.

    Args:
        verbose: print status
    Returns:
        True if reachable + credentials sign correctly, else False
    """
    try:
        result = aws_signed_request("health", "GET", verbose=verbose)
        return bool(result)
    except Exception:
        return False


def chat_with_persona(
    persona_id: str,
    message: str,
    conversation_id: str | None = None,
    verbose: bool = True,
) -> Optional[Tuple[str, str]]:
    """Send a message to a persona and return (response_text, conversation_id).

    Returns None on failure unless raise_on_error=True.
    """
    payload = {
        "persona_id": persona_id,
        "message": message,
        "conversation_id": conversation_id,
    }
    try:
        resp = aws_signed_request(
            path="chat",
            method="POST",
            payload=payload,
            verbose=verbose,
        )
        if not resp:
            return None
        data = resp.json()
        for key in ["response", "conversation_id", "conversation_count_week"]:
            if key not in data:
                raise RuntimeError(f"Chat response missing key '{key}'")
        if data["conversation_count_week"]:
            print(f"💬 Conversation count this week: {data['conversation_count_week']}")
        return data["response"], data["conversation_id"]
    except Exception as e:
        if verbose:
            print(f"❌ Chat failed: {e}")
        return None


def make_submission(
    results: List[Dict],
    dry_run: bool = False,
    verbose: bool = True,
) -> Optional[requests.Response]:
    """
    Submit results to GDSC challenge endpoint.

    Args:
        results: List of predictions in challenge format
        dry_run: If True, validate without submitting
        verbose: If True, print status messages

    Returns:
        API response or None if dry run

    Raises:
        ValueError: If results format is invalid

    Example:
        >>> results = generate_predictions()
        >>> response = make_submission(results, dry_run=True)  # Test first!
        >>> response = make_submission(results)  # Then submit
    """
    # Always validate first
    validate_submission_format(results)

    if dry_run:
        if verbose:
            print("🔍 Dry run mode - validating without submitting")
            print(f"✅ {len(results)} results are valid and ready to submit")
        return None

    try:
        response = aws_signed_request(
            path="submit",
            method="POST",
            payload={"submission": results},
            verbose=verbose,
        )
        if not response:
            return None
        if verbose:
            try:
                response_json = response.json()
                print("✅ Submission successful!")
                if response_json:
                    msg = response_json.get('message')
                    sid = response_json.get('submission_id')
                    scount = response_json.get('submission_count')
                    if msg:
                        print(f"📝 Server message: {msg}")
                    if sid:
                        print(f"🆔 Submission ID: {sid}")
                    if scount:
                        print(f"📊 Total submissions: {scount}")
            except ValueError:
                if verbose:
                    print("⚠️  Submission succeeded but response body was not JSON")
        return response
    except Exception as e:
        if verbose:
            print(f"❌ Submission failed: {e}")
        return None

def fetch_my_submissions(verbose: bool = True) -> Optional[List[Dict]]:
    """
    Fetch my team's submissions from GDSC challenge endpoint.

    Args:
        verbose: If True, print status messages

    Returns:
        API response or None if dry run

    Raises:
        ValueError: If my_submissions format is invalid

    Example:
        >>> my_submissions = fetch_my_submissions()
    """

    try:
        response = aws_signed_request(path="submit", method="GET", verbose=verbose)
        if not response:
            return None
        try:
            return response.json()
        except ValueError as e:
            raise RuntimeError("Failed to parse JSON for submissions list") from e
    except Exception as e:
        if verbose:
            print(f"❌ Fetch submissions failed: {e}")
        return None

def validate_submission_format(results: List[Dict]) -> None:
    """
    Validate submission format before sending.

    Good practice: Always validate before external API calls!

    Args:
        results: List of prediction dictionaries

    Raises:
        ValueError: If format is invalid
    """
    if not results:
        raise ValueError("Results list is empty")

    if len(results) != 100:
        print(f"⚠️  Warning: Expected 100 personas, got {len(results)}")

    required_fields = {'persona_id', 'predicted_type'}
    valid_types = {'jobs+trainings', 'trainings_only', 'awareness'}

    for i, result in enumerate(results):
        # Check required fields
        if not required_fields.issubset(result.keys()):
            missing = required_fields - result.keys()
            raise ValueError(f"Result {i} missing required fields: {missing}")

        # Check predicted_type
        pred_type = result['predicted_type']
        if pred_type not in valid_types:
            raise ValueError(
                f"Result {i} has invalid predicted_type: '{pred_type}'. "
                f"Must be one of: {valid_types}"
            )

        # Type-specific validation
        if pred_type == 'jobs+trainings':
            if 'jobs' not in result:
                raise ValueError(f"Result {i} missing 'jobs' field")
            if not isinstance(result['jobs'], list):
                raise ValueError(f"Result {i} 'jobs' must be a list")
            # Validate job structure
            for job in result['jobs']:
                if not isinstance(job, dict):
                    raise ValueError(f"Result {i} job items must be dictionaries")
                if 'job_id' not in job:
                    raise ValueError(f"Result {i} job missing 'job_id'")
                if 'suggested_trainings' not in job:
                    raise ValueError(f"Result {i} job missing 'suggested_trainings'")

        elif pred_type == 'trainings_only':
            if 'trainings' not in result:
                raise ValueError(f"Result {i} missing 'trainings' field")
            if not isinstance(result['trainings'], list):
                raise ValueError(f"Result {i} 'trainings' must be a list")

        elif pred_type == 'awareness':
            # awareness type can have optional predicted_items
            pass

    print(f"✅ Validated {len(results)} results - format is correct!")


def get_job_paths() -> List[Path]:
    """
    Discover all job description files in the dataset.

    Returns:
        List of Path objects for job files
    """
    data_dir = Path('./data/jobs')
    if not data_dir.exists():
        data_dir = Path('../data/jobs')  # Try parent directory

    if not data_dir.exists():
        raise FileNotFoundError(f"Jobs directory not found. Expected at: {data_dir}")

    paths = sorted([f for f in data_dir.iterdir() if f.suffix == '.md'])
    return paths


def get_training_paths() -> List[Path]:
    """
    Discover all training program files in the dataset.

    Returns:
        List of Path objects for training files
    """
    data_dir = Path('./data/trainings')
    if not data_dir.exists():
        data_dir = Path('../data/trainings')  # Try parent directory

    if not data_dir.exists():
        raise FileNotFoundError(f"Trainings directory not found. Expected at: {data_dir}")

    paths = sorted([f for f in data_dir.iterdir() if f.suffix == '.md'])
    return paths


# Cost tracking utilities for Mistral API usage
MISTRAL_PRICING = {
    'mistral-large-latest': {'input': 2.00, 'output': 6.00},  # per 1M tokens
    'mistral-medium-latest': {'input': 0.40, 'output': 2.00},  # per 1M tokens
    'mistral-small-latest': {'input': 0.10, 'output': 0.30},  # per 1M tokens
}

COST_TRACKER = {
    'api_calls': 0,
    'total_input_tokens': 0,
    'total_output_tokens': 0,
    'estimated_cost': 0.0,
    'by_model': {}
}


def calculate_cost(input_tokens: int, output_tokens: int, model: str = 'mistral-medium-latest') -> float:
    """
    Calculate actual cost based on Mistral's pricing.

    Args:
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        model: Mistral model identifier

    Returns:
        Estimated cost in USD
    """
    pricing = MISTRAL_PRICING.get(model, MISTRAL_PRICING['mistral-medium-latest'])
    input_cost = (input_tokens / 1_000_000) * pricing['input']
    output_cost = (output_tokens / 1_000_000) * pricing['output']
    return input_cost + output_cost


def track_api_call(response_or_model=None, input_tokens: int = 0, output_tokens: int = 0, model: str = None) -> float:
    """
    Track costs from Strands agent responses or direct token counts.

    Args:
        response_or_model: Either a response object from Strands agent OR a model string
        input_tokens: Number of input tokens (when passing model as first arg)
        output_tokens: Number of output tokens (when passing model as first arg)
        model: Mistral model identifier (when passing response as first arg)

    Usage:
        # With response object
        track_api_call(response, model='mistral-medium-latest')

        # With token counts
        track_api_call(model='mistral-medium-latest', input_tokens=500, output_tokens=50)

    Returns:
        Cost of this specific API call
    """
    # Handle different call signatures
    if isinstance(response_or_model, str):
        # Called with model as first argument
        model = response_or_model
    elif hasattr(response_or_model, 'metrics') and response_or_model.metrics:
        # Called with response object
        if model is None:
            model = 'mistral-medium-latest'
        input_tokens = response_or_model.metrics.accumulated_usage.get('inputTokens', 0)
        output_tokens = response_or_model.metrics.accumulated_usage.get('outputTokens', 0)
    else:
        # Default case
        if model is None:
            model = 'mistral-medium-latest'

    cost = calculate_cost(input_tokens, output_tokens, model)

    COST_TRACKER['api_calls'] += 1
    COST_TRACKER['total_input_tokens'] += input_tokens
    COST_TRACKER['total_output_tokens'] += output_tokens
    COST_TRACKER['estimated_cost'] += cost

    if model not in COST_TRACKER['by_model']:
        COST_TRACKER['by_model'][model] = {'calls': 0, 'cost': 0.0}
    COST_TRACKER['by_model'][model]['calls'] += 1
    COST_TRACKER['by_model'][model]['cost'] += cost

    return cost


def print_cost_summary():
    """Display running cost summary for API usage."""
    print("💰 Cost Summary:")
    print(f"  Total API calls: {COST_TRACKER['api_calls']}")
    print(f"  Total tokens: {COST_TRACKER['total_input_tokens'] + COST_TRACKER['total_output_tokens']:,}")
    print(f"  Estimated cost: ${COST_TRACKER['estimated_cost']:.4f}")

    if COST_TRACKER['by_model']:
        print("\n  By model:")
        for model, stats in COST_TRACKER['by_model'].items():
            print(f"    {model}: {stats['calls']} calls, ${stats['cost']:.4f}")


def reset_cost_tracker():
    """Reset the cost tracker to zero."""
    global COST_TRACKER
    COST_TRACKER = {
        'api_calls': 0,
        'total_input_tokens': 0,
        'total_output_tokens': 0,
        'estimated_cost': 0.0,
        'by_model': {}
    }
```

---

### <a name="green-agent-age-of-inference-ii-src-utils-matching_rules-py"></a>green-agent-age-of-inference-ii/src/utils/matching_rules.py

> 💬 **Developer Note:** OUR NEXT TARGET

**Size:** 6569 bytes

```python
import logging
from typing import Dict, Any, List

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Brazilian Education Levels Hierarchy ---
# A higher number indicates a higher level of education.
EDUCATION_LEVELS = {
    "Ensino Fundamental": 1,
    "Ensino Médio": 2,
    "Técnico": 3,
    "Tecnólogo": 4,
    "Graduação": 5,
    "Bacharelado": 5, # Equivalent to Graduação
    "Licenciatura": 5, # Equivalent to Graduação
    "Pós-graduação": 6,
    "Especialização": 6, # Equivalent to Pós-graduação
    "Mestrado": 7,
    "MBA": 7, # Often considered equivalent to Mestrado in a business context
    "Doutorado": 8,
    # Add common variations to handle messy data
    "ensino fundamental": 1,
    "ensino medio": 2,
    "tecnico": 3,
    "tecnologo": 4,
    "graduacao": 5,
    "bacharelado": 5,
    "licenciatura": 5,
    "pos-graduacao": 6,
    "especializacao": 6,
    "mestrado": 7,
    "mba": 7,
    "doutorado": 8,
}

# def apply_hard_filters(persona: Dict[str, Any], job: Dict[str, Any]) -> bool:
#     """
#     Applies strict matching rules to determine if a job is a fit for a persona.

#     Args:
#         persona: A dictionary representing the persona's profile.
#         job: A dictionary representing the job's requirements.

#     Returns:
#         True if the job passes all hard filters, False otherwise.
#     """
#     # 1. Location Filter
#     is_job_remote = job.get("is_remote", False)
#     persona_open_to_relocate = persona.get("is_open_to_relocate", False)
#     if not is_job_remote and not persona_open_to_relocate:
#         if persona.get("city") != job.get("city"):
#             logger.debug(f"Filter FAIL (Location): Job city {job.get('city')} != Persona city {persona.get('city')}")
#             return False

#     # 2. Education Filter
#     persona_edu_level = EDUCATION_LEVELS.get(persona.get("education_level", "").strip(), 0)
#     job_edu_req = EDUCATION_LEVELS.get(job.get("education_level", "").strip(), 0)
#     if persona_edu_level < job_edu_req:
#         logger.debug(f"Filter FAIL (Education): Persona level {persona_edu_level} < Job level {job_edu_req}")
#         return False
        
#     # # 3. Experience Filter
#     # persona_exp = persona.get("experience_years", 0)
#     # job_exp_req = job.get("experience_years", 0)
#     # if persona_exp < job_exp_req:
#     #     logger.debug(f"Filter FAIL (Experience): Persona years {persona_exp} < Job years {job_exp_req}")
#     #     return False
    
#     # 3. Experience Filter (with tolerance for entry-level)
#     persona_exp = persona.get("experience_years", 0)
#     job_exp_req = job.get("experience_years", 0)
    
#     # NEW LOGIC: If a job requires 1 year or less, consider it entry-level
#     # and allow candidates with 0 experience.
#     if job_exp_req <= 1 and persona_exp == 0:
#         pass # This is an acceptable entry-level match, so we don't fail.
#     elif persona_exp < job_exp_req:
#         logger.debug(f"Filter FAIL (Experience): Persona years {persona_exp} < Job years {job_exp_req}")
#         return False

#     # 4. Language Filter (simplified: checks for at least one common language)
#     persona_langs = set(lang.lower() for lang in persona.get("languages", []))
#     job_langs_req = set(lang.lower() for lang in job.get("languages", []))
#     if job_langs_req and not persona_langs.intersection(job_langs_req):
#         logger.debug(f"Filter FAIL (Language): No common language between {persona_langs} and {job_langs_req}")
#         return False

#     # If all checks pass
#     logger.debug("Filter PASS: All hard filters met.")
#     return True

from typing import Tuple

def apply_hard_filters(persona: Dict[str, Any], job: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Applies strict matching rules.

    Returns:
        A tuple containing (True, "OK") if the job passes,
        or (False, "Reason for failure") otherwise.
    """
    # 1. Location Filter
    is_job_remote = job.get("is_remote", False)
    persona_open_to_relocate = persona.get("is_open_to_relocate", False)
    if not is_job_remote and not persona_open_to_relocate:
        if persona.get("city") != job.get("city"):
            return False, f"Location Mismatch: Persona city '{persona.get('city')}' vs Job city '{job.get('city')}'"

    # 2. Education Filter
    persona_edu_level = EDUCATION_LEVELS.get(persona.get("education_level", "").strip(), 0)
    job_edu_req = EDUCATION_LEVELS.get(job.get("education_level", "").strip(), 0)
    if persona_edu_level < job_edu_req:
        return False, f"Education Mismatch: Persona level {persona_edu_level} < Job level {job_edu_req}"
        
    # 3. Experience Filter (with tolerance for entry-level)
    persona_exp = persona.get("experience_years", 0)
    job_exp_req = job.get("experience_years", 0)
    if job_exp_req <= 1 and persona_exp == 0:
        pass
    elif persona_exp < job_exp_req:
        return False, f"Experience Mismatch: Persona years {persona_exp} < Job years {job_exp_req}"

    # 4. Language Filter
    persona_langs = set(lang.lower() for lang in persona.get("languages", []))
    job_langs_req = set(lang.lower() for lang in job.get("languages", []))
    if job_langs_req and not persona_langs.intersection(job_langs_req):
        return False, f"Language Mismatch: Persona langs {persona_langs} vs Job langs {job_langs_req}"

    # If all checks pass
    return True, "OK"

def get_required_trainings(persona: Dict[str, Any], job: Dict[str, Any]) -> List[str]:
    """
    Identifies trainings needed for a persona to meet job skill requirements.
    
    NOTE: This is a simplified initial implementation. It only identifies missing
    skills and does not yet handle the sequential level progression.

    Args:
        persona: A dictionary representing the persona's profile.
        job: A dictionary representing the job's requirements.

    Returns:
        A list of skill names for which training is required.
    """
    persona_skills = set(skill.lower() for skill in persona.get("skills", []))
    job_skills_req = set(skill.lower() for skill in job.get("required_skills", []))
    
    missing_skills = list(job_skills_req - persona_skills)
    logger.debug(f"Identified missing skills: {missing_skills}")
    return missing_skills

```

---

### <a name="green-agent-age-of-inference-ii-src-utils-s3_helper-py"></a>green-agent-age-of-inference-ii/src/utils/s3_helper.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-__init__-py"></a>green-agent-age-of-inference-ii/tests/__init__.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_call_llm-py"></a>green-agent-age-of-inference-ii/tests/test_call_llm.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_data_retrieval-py"></a>green-agent-age-of-inference-ii/tests/test_data_retrieval.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_integration-py"></a>green-agent-age-of-inference-ii/tests/test_integration.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_matching-py"></a>green-agent-age-of-inference-ii/tests/test_matching.py

> 💬 **Developer Note:** OUR NEXT TARGET TEST

**Size:** 0 bytes

```python

```

---

### <a name="green-agent-age-of-inference-ii-tests-test_matching_rules-py"></a>green-agent-age-of-inference-ii/tests/test_matching_rules.py

> 💬 **Developer Note:** Y

**Size:** 3984 bytes

```python
import pytest
from src.utils.matching_rules import apply_hard_filters, get_required_trainings

# --- Test Data Fixtures ---
@pytest.fixture
def sample_persona():
    """A sample persona profile for testing."""
    return {
        "city": "São Paulo",
        "education_level": "Graduação",
        "experience_years": 3,
        "languages": ["Portuguese", "English"],
        "is_open_to_relocate": False,
        "skills": ["Python", "Data Analysis"]
    }

@pytest.fixture
def sample_job():
    """A perfectly matching job for the sample persona."""
    return {
        "city": "São Paulo",
        "is_remote": False,
        "education_level": "Graduação",
        "experience_years": 2,
        "languages": ["Portuguese"],
        "required_skills": ["Python", "SQL"]
    }

# --- Tests for apply_hard_filters ---

def test_filters_pass_on_perfect_match(sample_persona, sample_job):
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_location(sample_persona, sample_job):
    sample_job["city"] = "Recife"
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_location_if_remote(sample_persona, sample_job):
    sample_job["city"] = "Recife"
    sample_job["is_remote"] = True
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_passes_on_location_if_relocate(sample_persona, sample_job):
    sample_persona["is_open_to_relocate"] = True
    sample_job["city"] = "Recife"
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_education(sample_persona, sample_job):
    sample_job["education_level"] = "Mestrado"
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_lower_education_req(sample_persona, sample_job):
    sample_job["education_level"] = "Técnico"
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_experience(sample_persona, sample_job):
    sample_job["experience_years"] = 5
    assert apply_hard_filters(sample_persona, sample_job) == False
    
def test_filter_fails_on_language(sample_persona, sample_job):
    sample_job["languages"] = ["Spanish"]
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_language_intersection(sample_persona, sample_job):
    sample_job["languages"] = ["English", "Spanish"]
    assert apply_hard_filters(sample_persona, sample_job) == True

# --- Tests for get_required_trainings ---

def test_trainings_identifies_missing_skill(sample_persona, sample_job):
    missing = get_required_trainings(sample_persona, sample_job)
    assert isinstance(missing, list)
    assert len(missing) == 1
    assert "sql" in missing

def test_trainings_returns_empty_when_no_skills_missing(sample_persona, sample_job):
    sample_persona["skills"].append("SQL")
    missing = get_required_trainings(sample_persona, sample_job)
    assert len(missing) == 0

def test_trainings_returns_empty_when_job_has_no_reqs(sample_persona, sample_job):
    sample_job["required_skills"] = []
    missing = get_required_trainings(sample_persona, sample_job)
    assert len(missing) == 0

# --- NEW ---
def test_filter_passes_on_experience_with_tolerance(sample_persona, sample_job):
    """
    Tests that a persona with 0 experience CAN match a job requiring 1 year,
    due to our new tolerance rule for entry-level positions.
    """
    # Arrange
    sample_persona["experience_years"] = 0
    sample_job["experience_years"] = 1 # Job requires 1 year

    # Act & Assert
    assert apply_hard_filters(sample_persona, sample_job) == True, \
        "Should PASS: Persona with 0 exp should match job with 1 yr req."
    
    # Also test the boundary condition
    sample_job["experience_years"] = 2 # Job requires 2 years
    assert apply_hard_filters(sample_persona, sample_job) == False, \
        "Should FAIL: Tolerance should not apply to jobs requiring > 1 yr exp."

```

---

### <a name="green-agent-age-of-inference-ii-tests-test_nodes-py"></a>green-agent-age-of-inference-ii/tests/test_nodes.py

**Size:** 21774 bytes

```python
import pytest
import os
import json
import getpass
from pathlib import Path
from src.nodes import LoadStaticDataNode, ExtractProfileNode, DecisionNode, ParseStaticDataNode, PersonaProfile, JobProfile, TrainingProfile
from src.utils.matching_rules import EDUCATION_LEVELS
from dotenv import load_dotenv
from src.utils.gdsc_utils import sanity_check

# --- Load .env file for MISTRAL_API_KEY ---
load_dotenv()


# --- REFACTORED: Credential Loading as a Fixture ---
@pytest.fixture(scope="session", autouse=True)
def manage_credentials(request):
    """
    A session-wide fixture to manage credentials. It only prompts for AWS
    credentials if a test marked with 'requires_aws_creds' is selected to run.
    """
    if request.node.get_closest_marker("requires_aws_creds"):
        print("\n(An AWS-dependent test is running, checking credentials...)")
        creds_to_check = {
            "AWS_ACCESS_KEY_ID": "Enter your AWS Access Key ID: ",
            "AWS_SECRET_ACCESS_KEY": "Enter your AWS Secret Access Key: ",
            "AWS_SESSION_TOKEN": "Enter your AWS Session Token: "
        }
        for key, prompt_text in creds_to_check.items():
            if not os.getenv(key):
                print(f"Environment variable '{key}' not found.")
                value = getpass.getpass(prompt_text)
                os.environ[key] = value
                print(f"✅ '{key}' set for this session.")

# This marker will now trigger the fixture above.
requires_aws_creds = pytest.mark.skipif(
    not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"),
    reason="This test makes a live API call and requires AWS credentials."
)
# Ensure Mistral key is present for tests that need it.
requires_mistral_key = pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="This test requires the MISTRAL_API_KEY."
)

# --- Fixture to clean up cache files ---
@pytest.fixture
def cleanup_cache_files():
    yield
    print("\nCleaning up cache files...")
    job_cache = Path("data/parsed_jobs.json")
    training_cache = Path("data/parsed_trainings.json")
    if job_cache.exists():
        job_cache.unlink()
        print("Removed job cache.")
    if training_cache.exists():
        training_cache.unlink()
        print("Removed training cache.")

# # --- OPTIMIZED: Test for ParseStaticDataNode ---
# @requires_mistral_key
# def test_parse_static_data_node(cleanup_cache_files):
#     """
#     Tests the ParseStaticDataNode on a small subset of data.
#     It verifies both parsing from markdown and reading from the created cache.
#     """
#     # Arrange: Create a small subset of the real data for testing
#     load_node = LoadStaticDataNode()
#     shared_full = {}
#     load_node.run(shared_full)
    
#     # OPTIMIZATION: Use only a small slice of the data
#     test_jobs_raw = shared_full["all_jobs"][:5]
#     test_trainings_raw = shared_full["all_trainings"][:5]
    
#     # --- 1. First Run: Parsing the subset ---
#     print("\n--- Running ParseStaticDataNode (First Run): Parsing 5 jobs & 5 trainings ---")
#     shared = {"all_jobs": test_jobs_raw, "all_trainings": test_trainings_raw}
#     parse_node = ParseStaticDataNode()
#     parse_node.shared = shared
#     parse_node.run(shared)

#     # Assert parsing worked and cache files were created
#     assert "parsed_jobs" in shared
#     assert "parsed_trainings" in shared
#     assert len(shared["parsed_jobs"]) == 5
#     assert len(shared["parsed_trainings"]) == 5
#     assert isinstance(shared["parsed_jobs"][0], JobProfile)
#     assert isinstance(shared["parsed_trainings"][0], TrainingProfile)
#     assert Path("data/parsed_jobs.json").exists()
#     assert Path("data/parsed_trainings.json").exists()

#     # --- 2. Second Run: Reading from cache ---
#     print("\n--- Running ParseStaticDataNode (Second Run): Reading from cache ---")
#     shared_cached = {"all_jobs": test_jobs_raw, "all_trainings": test_trainings_raw}
#     parse_node_cached = ParseStaticDataNode()
#     parse_node_cached.shared = shared_cached
#     parse_node_cached.run(shared_cached)

#     # Assert data was loaded from cache correctly
#     assert len(shared_cached["parsed_jobs"]) == 5
#     assert len(shared_cached["parsed_trainings"]) == 5
#     assert shared_cached["parsed_jobs"][0].job_id == shared["parsed_jobs"][0].job_id

# ADD THIS NEW TEST to tests/test_nodes.py
@requires_mistral_key
@pytest.mark.parametrize("model_name, suffix", [
    ("mistral-small-latest", "_small"),
    ("mistral-large-latest", "_large"),
])
def test_parse_static_data_node_model_comparison(model_name, suffix):
    """
    Tests the ParseStaticDataNode with different models on a small data sample.
    It saves the output to separate cache files for quality comparison and
    validates that no Pydantic errors occur.
    """
    # 1. Arrange: Create a small subset of raw data for the test
    sample_jobs_raw = [
        {'id': 'j0', 'content': Path('data/jobs/j0.md').read_text()},
        {'id': 'j1', 'content': Path('data/jobs/j1.md').read_text()}
    ]
    sample_trainings_raw = [
        {'id': 'tr0', 'content': Path('data/trainings/tr0.md').read_text()},
        {'id': 'tr1', 'content': Path('data/trainings/tr1.md').read_text()}
    ]
    
    # Clean up any old cache files before the test
    job_cache = Path(f"data/parsed_jobs{suffix}.json")
    if job_cache.exists():
        job_cache.unlink()
        
    training_cache = Path(f"data/parsed_trainings{suffix}.json")
    if training_cache.exists():
        training_cache.unlink()

    # 2. Act: Run the node with the specified model and cache suffix
    shared = {"all_jobs": sample_jobs_raw, "all_trainings": sample_trainings_raw}
    node = ParseStaticDataNode()
    node.set_params({
        "parsing_model": model_name,
        "cache_suffix": suffix
    })
    
    print(f"\n--- Testing parsing with model: {model_name} ---")
    
    # This will raise an exception if Pydantic validation fails, causing the test to fail.
    node.run(shared)

    # 3. Assert: Check that the process completed and created valid objects
    assert "parsed_jobs" in shared
    assert "parsed_trainings" in shared
    assert len(shared["parsed_jobs"]) == 2
    assert len(shared["parsed_trainings"]) == 2
    
    # Check that the objects are of the correct type (Pydantic validation passed)
    assert isinstance(shared["parsed_jobs"][0], JobProfile)
    assert isinstance(shared["parsed_trainings"][0], TrainingProfile)
    
    # Check that the cache files were created
    assert job_cache.exists()
    assert training_cache.exists()

    print(f"--- ✅ Success! Parsed successfully with {model_name}. ---")
    print(f"--- Output saved to {job_cache} and {training_cache} ---")

def test_load_static_data_node():
    node = LoadStaticDataNode()
    shared = {}
    node.run(shared)
    assert "all_jobs" in shared
    assert "all_trainings" in shared
    assert len(shared["all_jobs"]) == 200
    assert len(shared["all_trainings"]) == 497

# --- Helper function for credential checking ---
def check_and_get_aws_credentials():
    """Checks for AWS credentials, prompts if necessary, and returns True if ready."""
    if all(os.getenv(key) for key in ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]):
        print("\n✅ AWS credentials found in environment.")
        return True

    print("\n🔑 AWS Credential Check")
    is_interactive = os.isatty(0)
    
    if is_interactive:
        response = input("Are you in an environment with an IAM role (e.g., SageMaker)? [y/n]: ").lower()
    else:
        print("Non-interactive environment detected. Assuming IAM role.")
        response = 'y'

    if response == 'y':
        print("Proceeding with IAM role-based authentication.")
        try:
            if not sanity_check(verbose=False):
                print("⚠️ Warning: Sanity check to AWS failed with IAM role.")
        except Exception as e:
            print(f"⚠️ Warning: Sanity check to AWS failed: {e}")
        return True # Assume role is present and let the API call try
    else:
        print("🔧 Please provide temporary AWS credentials.")
        # Using getpass to hide secret key input
        key_id = input("Enter AWS Access Key ID: ")
        secret_key = getpass.getpass("Enter AWS Secret Access Key: ")
        token = getpass.getpass("Enter AWS Session Token: ")
        if not all([key_id, secret_key, token]):
            print("❌ Incomplete credentials provided.")
            return False
        os.environ["AWS_ACCESS_KEY_ID"] = key_id
        os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key
        os.environ["AWS_SESSION_TOKEN"] = token
        print("✅ Manual credentials set for this session.")
        return True

@requires_mistral_key # We still need the Mistral key
def test_extract_profile_node_dynamic_live():
    """
    Performs a live, end-to-end test of the dynamic ExtractProfileNode.
    It now interactively checks for credentials and allows persona selection.
    """
    # 1. Credential Check
    if not check_and_get_aws_credentials():
        pytest.skip("AWS credentials were not provided. Skipping live test.")

    # 2. Persona Selection
    persona_num_str = input("\nEnter a persona number to test (1-100): ")
    try:
        persona_num = int(persona_num_str)
        if not 1 <= persona_num <= 100:
            raise ValueError
        persona_to_test = f"persona_{persona_num:03d}"
    except (ValueError, TypeError):
        default_persona = "persona_001"
        print(f"Invalid input. Defaulting to {default_persona}.")
        persona_to_test = default_persona
    
    # 3. Arrange
    node = ExtractProfileNode()
    shared = {"persona_id": persona_to_test}
    
    print(f"\n--- Starting LIVE dynamic conversation test for {persona_to_test} ---")

    # 4. Act
    node.run(shared)

    # 5. Assert
    assert "persona_profile" in shared
    profile = shared["persona_profile"]
    assert isinstance(profile, PersonaProfile)
    
    assert "conversation_history" in shared
    assert len(shared["conversation_history"]) > 0
    
    print(f"\n--- Live Test Complete for {persona_to_test} ---")
    print("Final Extracted Profile:")
    print(profile.model_dump_json(indent=2))
    print("\nConversation History:")
    for turn in shared["conversation_history"]:
        print(f"  Q: {turn['question']}")
        print(f"  A: {turn['answer']}")

from src.nodes import ProvideAwarenessNode

@pytest.mark.parametrize("decision_action, expected_reason", [
    ("provide_awareness_young", "too_young"),
    ("provide_awareness_info", "info"),
])
def test_provide_awareness_node(decision_action, expected_reason):
    """
    Tests that the ProvideAwarenessNode correctly formats the output
    for both 'too_young' and 'info' scenarios.
    """
    # Arrange
    node = ProvideAwarenessNode()
    shared = {"decision_action": decision_action}

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recommendation = shared["intermediate_recommendations"]
    assert recommendation["predicted_type"] == "awareness"
    assert recommendation["predicted_items"] == expected_reason

from src.nodes import FindTrainingsOnlyNode

def test_find_trainings_only_node():
    """
    Tests that the FindTrainingsOnlyNode correctly identifies trainings
    that are the immediate next step OR are open to all levels.
    """
    # Arrange
    node = FindTrainingsOnlyNode()
    
    # mock_persona = PersonaProfile(
    #     age=20, city="Test", education_level="Ensino Médio", # Level 2
    #     experience_years=1, skills=[], goals="learn", is_open_to_relocate=False
    # )
    mock_persona = PersonaProfile(
        persona_id="test_persona_01",
        age=20, city="Test", education_level="Ensino Médio", # Level 2
        experience_years=1, skills=[], goals="learn", is_open_to_relocate=False
    )
    
    # CORRECTED: Added 'offered_skills' to each mock profile
    mock_trainings = [
        TrainingProfile(training_id="tr1", title="Basic Course", offered_skills=["skill1"], required_level="Ensino Fundamental"), # Level 1 (too low)
        TrainingProfile(training_id="tr2", title="Technical Intro", offered_skills=["skill2"], required_level="Técnico"),         # Level 3 (correct next step)
        TrainingProfile(training_id="tr3", title="Another Tech", offered_skills=["skill3"], required_level="Técnico"),          # Level 3 (correct next step)
        TrainingProfile(training_id="tr4", title="Advanced Degree", offered_skills=["skill4"], required_level="Graduação"),      # Level 5 (too high)
        TrainingProfile(training_id="tr5", title="Open for All", offered_skills=["skill5"], required_level=None),               # Level 0 (correct, open)
    ]
    
    shared = {
        "persona_profile": mock_persona,
        "parsed_trainings": mock_trainings
    }

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recommendation = shared["intermediate_recommendations"]
    
    recommended_ids = {t["training_id"] for t in recommendation["trainings"]}
    assert len(recommended_ids) == 3
    assert "tr2" in recommended_ids # Next level
    assert "tr3" in recommended_ids # Next level
    assert "tr5" in recommended_ids # Open to all
    assert "tr1" not in recommended_ids
    assert "tr4" not in recommended_ids

from src.nodes import FindJobsAndTrainingsNode

# ADDED to: tests/test_nodes.py

@pytest.fixture(scope="session")
@requires_mistral_key
def live_parsed_data():
    """
    A session-scoped fixture that runs the initial data loading and parsing nodes
    ONCE to provide real, parsed data for live tests.
    This avoids re-parsing for every test function.
    """
    print("\n--- (Fixture) Loading and parsing all static data for live tests... ---")
    # Use existing cache if available, otherwise parse fresh
    job_cache_path = Path("data/parsed_jobs.json")
    training_cache_path = Path("data/parsed_trainings.json")

    shared = {}
    if job_cache_path.exists() and training_cache_path.exists():
        print("--- (Fixture) Found existing cache. Loading parsed data directly. ---")
        with open(job_cache_path, 'r', encoding='utf-8') as f:
            shared["parsed_jobs"] = [JobProfile.model_validate(item) for item in json.load(f)]
        with open(training_cache_path, 'r', encoding='utf-8') as f:
            shared["parsed_trainings"] = [TrainingProfile.model_validate(item) for item in json.load(f)]
    else:
        print("--- (Fixture) No cache found. Performing full load and parse... ---")
        load_node = LoadStaticDataNode()
        load_node.run(shared)
        
        parse_node = ParseStaticDataNode()
        parse_node.shared = shared
        parse_node.run(shared)
    
    if not shared.get("parsed_jobs") or not shared.get("parsed_trainings"):
        pytest.fail("Data parsing failed in the fixture. Cannot proceed with live tests.")
        
    print(f"--- (Fixture) Data ready: {len(shared['parsed_jobs'])} jobs, {len(shared['parsed_trainings'])} trainings. ---")
    return shared

@requires_mistral_key
def test_find_jobs_and_trainings_node_live_with_large_model(live_parsed_data):
    """
    Tests the FindJobsAndTrainingsNode with REAL data, NO CACHE, and the
    POWERFUL mistral-large-latest model to ensure the highest quality reasoning.
    """
    # 1. Arrange
    node = FindJobsAndTrainingsNode()
    # THIS IS THE KEY CHANGE: Use the large model and disable cache
    node.set_params({
        "use_cache_for_scoring": False,
        "scoring_model": "mistral-large-latest"
    })
    
    # persona = PersonaProfile(
    #     age=25,
    #     city="São Paulo",
    #     education_level="Graduação",
    #     experience_years=2,
    #     skills=["Análise de Dados", "Relatórios Financeiros"],
    #     goals="Busco uma oportunidade como analista de dados no setor financeiro ou de sustentabilidade.",
    #     is_open_to_relocate=False,
    #     languages=["Portuguese", "English"]
    # )
    persona = PersonaProfile(
        persona_id="test_persona_02",
        age=25,
        city="São Paulo",
        education_level="Graduação",
        experience_years=2,
        skills=["Análise de Dados", "Relatórios Financeiros"],
        goals="Busco uma oportunidade como analista de dados no setor financeiro ou de sustentabilidade.",
        is_open_to_relocate=False,
        languages=["Portuguese", "English"]
    )
    
    shared = live_parsed_data.copy()
    shared["persona_profile"] = persona
    
    print(f"\n--- Starting LIVE scoring test (Large Model, No Cache) for persona goals: '{persona.goals}' ---")
    
    # 2. Act
    node.run(shared)
    
    # 3. Assert and Inspect
    assert "intermediate_recommendations" in shared
    recs = shared["intermediate_recommendations"]
    assert recs["predicted_type"] == "jobs+trainings"
    
    num_recommendations = len(recs["jobs"])
    print(f"Node returned {num_recommendations} job recommendations.")
    assert 0 < num_recommendations <= 3

    print("\n--- Top Recommendations (Scored with mistral-large-latest) ---")
    for job_rec in recs["jobs"]:
        job_id = job_rec['job_id']
        job_profile = next((j for j in shared['parsed_jobs'] if j.job_id == job_id), None)
        title = job_profile.title if job_profile else "Unknown Title"
        print(f"\nJob ID: {job_id} ({title})")
        if job_rec['suggested_trainings']:
            for training_suggestion in job_rec['suggested_trainings']:
                print(f"  - Missing Skill: {training_suggestion['missing_skill']}")
                print(f"    - Suggested Trainings: {[t['training_id'] for t in training_suggestion['trainings']]}")
        else:
            print("  - No skill gaps identified.")

from src.nodes import FinalizeOutputNode

@pytest.mark.parametrize("intermediate_recs", [
    # Case 1: Awareness
    ({"predicted_type": "awareness", "predicted_items": "too_young"}),
    # Case 2: Trainings Only
    ({"predicted_type": "trainings_only", "trainings": [{"training_id": "tr1"}]}),
    # Case 3: Jobs + Trainings
    ({"predicted_type": "jobs+trainings", "jobs": [{"job_id": "j1", "suggested_trainings": []}]}),
])
def test_finalize_output_node(intermediate_recs):
    """
    Tests that the FinalizeOutputNode correctly merges the persona_id
    with the recommendation payload from any of the logic branches.
    """
    # Arrange
    node = FinalizeOutputNode()
    shared = {
        "persona_id": "persona_test_123",
        "intermediate_recommendations": intermediate_recs
    }

    # Act
    node.run(shared)

    # Assert
    assert "final_recommendation" in shared
    final_rec = shared["final_recommendation"]

    # Check that persona_id is present and correct
    assert "persona_id" in final_rec
    assert final_rec["persona_id"] == "persona_test_123"

    # Check that all keys from the intermediate recs are present
    for key, value in intermediate_recs.items():
        assert key in final_rec
        assert final_rec[key] == value

from unittest.mock import MagicMock

def test_find_trainings_only_node_with_domain_filter(monkeypatch):
    """
    Tests the full three-stage filtering logic of the FindTrainingsOnlyNode.
    - Mocks the new domain classification method.
    - Mocks the final scoring method.
    - Asserts that only trainings passing all filters are recommended.
    """
    # Arrange
    node = FindTrainingsOnlyNode()
    
    # mock_persona = PersonaProfile(
    #     age=20, city="Test", education_level="Ensino Médio", # Level 2
    #     experience_years=1, skills=[], goals="learn about technology", is_open_to_relocate=False
    # )
    mock_persona = PersonaProfile(
        persona_id="test_persona_03",
        age=20, city="Test", education_level="Ensino Médio", # Level 2
        experience_years=1, skills=[], goals="learn about technology", is_open_to_relocate=False
    )
    
    mock_trainings = [
        TrainingProfile(training_id="tr1", title="Basic Tech Course", offered_skills=["tech"], required_level="Técnico"),         # Eligible and relevant
        TrainingProfile(training_id="tr2", title="Advanced Cooking", offered_skills=["cooking"], required_level="Técnico"),      # Eligible but NOT relevant
        TrainingProfile(training_id="tr3", title="Intro to IT", offered_skills=["it"], required_level=None),                   # Eligible and relevant
        TrainingProfile(training_id="tr4", title="Post-grad Finance", offered_skills=["finance"], required_level="Graduação"),  # NOT eligible
    ]
    
    shared = {
        "persona_profile": mock_persona,
        "parsed_trainings": mock_trainings
    }

    # Mock the new domain classification method
    def mock_domain_check(goals, training):
        # Only return True for trainings with "tech" or "it" in the title
        return "tech" in training.title.lower() or "it" in training.title.lower()
        
    monkeypatch.setattr(node, '_is_training_relevant_domain', mock_domain_check)

    # Mock the final scoring method to return a consistent score
    monkeypatch.setattr(node, '_get_training_relevance_score', lambda persona, training: 8)

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recommendation = shared["intermediate_recommendations"]
    
    recommended_ids = {t["training_id"] for t in recommendation["trainings"]}
    assert len(recommended_ids) == 2
    assert "tr1" in recommended_ids # Was eligible and passed domain filter
    assert "tr3" in recommended_ids # Was eligible and passed domain filter
    assert "tr2" not in recommended_ids # Was eligible but FAILED domain filter
    assert "tr4" not in recommended_ids # Was NOT eligible
```

---

### <a name="green-agent-age-of-inference-ii-tests-test_utils-py"></a>green-agent-age-of-inference-ii/tests/test_utils.py

**Size:** 0 bytes

```python

```

---

