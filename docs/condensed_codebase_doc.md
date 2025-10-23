# Python Codebase Documentation

**Root Directory:** `/home/ec2-user/SageMaker/green-agent-age-of-inference-ii`
**Total Python Files:** 18

---

## 📂 Project Structure

```
📁 green-agent-age-of-inference-ii/
├── 📁 data/
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
│   └── 📁 trainings/
│       ├── 📄 tr0.md
│       ├── 📄 tr1.md
│       ├── 📄 tr10.md
│       ├── 📄 tr100.md
│       ├── 📄 tr101.md
│       ├── 📄 tr102.md
│       ├── 📄 tr103.md
│       ├── 📄 tr104.md
│       ├── 📄 tr105.md
│       ├── 📄 tr106.md
│       ├── 📄 tr107.md
│       ├── 📄 tr108.md
│       ├── 📄 tr109.md
│       ├── 📄 tr11.md
│       ├── 📄 tr110.md
│       ├── 📄 tr111.md
│       ├── 📄 tr112.md
│       ├── 📄 tr113.md
│       ├── 📄 tr114.md
│       ├── 📄 tr115.md
│       ├── 📄 tr116.md
│       ├── 📄 tr117.md
│       ├── 📄 tr118.md
│       ├── 📄 tr119.md
│       ├── 📄 tr12.md
│       ├── 📄 tr120.md
│       ├── 📄 tr121.md
│       ├── 📄 tr122.md
│       ├── 📄 tr123.md
│       ├── 📄 tr124.md
│       ├── 📄 tr125.md
│       ├── 📄 tr126.md
│       ├── 📄 tr127.md
│       ├── 📄 tr128.md
│       ├── 📄 tr129.md
│       ├── 📄 tr13.md
│       ├── 📄 tr130.md
│       ├── 📄 tr131.md
│       ├── 📄 tr132.md
│       ├── 📄 tr133.md
│       ├── 📄 tr134.md
│       ├── 📄 tr135.md
│       ├── 📄 tr136.md
│       ├── 📄 tr137.md
│       ├── 📄 tr138.md
│       ├── 📄 tr139.md
│       ├── 📄 tr14.md
│       ├── 📄 tr140.md
│       ├── 📄 tr141.md
│       ├── 📄 tr142.md
│       ├── 📄 tr143.md
│       ├── 📄 tr144.md
│       ├── 📄 tr145.md
│       ├── 📄 tr146.md
│       ├── 📄 tr147.md
│       ├── 📄 tr148.md
│       ├── 📄 tr149.md
│       ├── 📄 tr15.md
│       ├── 📄 tr150.md
│       ├── 📄 tr151.md
│       ├── 📄 tr152.md
│       ├── 📄 tr153.md
│       ├── 📄 tr154.md
│       ├── 📄 tr155.md
│       ├── 📄 tr156.md
│       ├── 📄 tr157.md
│       ├── 📄 tr158.md
│       ├── 📄 tr159.md
│       ├── 📄 tr16.md
│       ├── 📄 tr160.md
│       ├── 📄 tr161.md
│       ├── 📄 tr162.md
│       ├── 📄 tr163.md
│       ├── 📄 tr164.md
│       ├── 📄 tr165.md
│       ├── 📄 tr166.md
│       ├── 📄 tr167.md
│       ├── 📄 tr168.md
│       ├── 📄 tr169.md
│       ├── 📄 tr17.md
│       ├── 📄 tr170.md
│       ├── 📄 tr171.md
│       ├── 📄 tr172.md
│       ├── 📄 tr173.md
│       ├── 📄 tr174.md
│       ├── 📄 tr175.md
│       ├── 📄 tr176.md
│       ├── 📄 tr177.md
│       ├── 📄 tr178.md
│       ├── 📄 tr179.md
│       ├── 📄 tr18.md
│       ├── 📄 tr180.md
│       ├── 📄 tr181.md
│       ├── 📄 tr182.md
│       ├── 📄 tr183.md
│       ├── 📄 tr184.md
│       ├── 📄 tr185.md
│       ├── 📄 tr186.md
│       ├── 📄 tr187.md
│       ├── 📄 tr188.md
│       ├── 📄 tr189.md
│       ├── 📄 tr19.md
│       ├── 📄 tr190.md
│       ├── 📄 tr191.md
│       ├── 📄 tr192.md
│       ├── 📄 tr193.md
│       ├── 📄 tr194.md
│       ├── 📄 tr195.md
│       ├── 📄 tr196.md
│       ├── 📄 tr197.md
│       ├── 📄 tr198.md
│       ├── 📄 tr199.md
│       ├── 📄 tr2.md
│       ├── 📄 tr20.md
│       ├── 📄 tr200.md
│       ├── 📄 tr201.md
│       ├── 📄 tr202.md
│       ├── 📄 tr203.md
│       ├── 📄 tr204.md
│       ├── 📄 tr205.md
│       ├── 📄 tr206.md
│       ├── 📄 tr207.md
│       ├── 📄 tr208.md
│       ├── 📄 tr209.md
│       ├── 📄 tr21.md
│       ├── 📄 tr210.md
│       ├── 📄 tr211.md
│       ├── 📄 tr212.md
│       ├── 📄 tr213.md
│       ├── 📄 tr214.md
│       ├── 📄 tr215.md
│       ├── 📄 tr216.md
│       ├── 📄 tr217.md
│       ├── 📄 tr218.md
│       ├── 📄 tr219.md
│       ├── 📄 tr22.md
│       ├── 📄 tr220.md
│       ├── 📄 tr221.md
│       ├── 📄 tr222.md
│       ├── 📄 tr223.md
│       ├── 📄 tr224.md
│       ├── 📄 tr225.md
│       ├── 📄 tr226.md
│       ├── 📄 tr227.md
│       ├── 📄 tr228.md
│       ├── 📄 tr229.md
│       ├── 📄 tr23.md
│       ├── 📄 tr230.md
│       ├── 📄 tr231.md
│       ├── 📄 tr232.md
│       ├── 📄 tr233.md
│       ├── 📄 tr234.md
│       ├── 📄 tr235.md
│       ├── 📄 tr236.md
│       ├── 📄 tr237.md
│       ├── 📄 tr238.md
│       ├── 📄 tr239.md
│       ├── 📄 tr24.md
│       ├── 📄 tr240.md
│       ├── 📄 tr241.md
│       ├── 📄 tr242.md
│       ├── 📄 tr243.md
│       ├── 📄 tr244.md
│       ├── 📄 tr245.md
│       ├── 📄 tr246.md
│       ├── 📄 tr247.md
│       ├── 📄 tr248.md
│       ├── 📄 tr249.md
│       ├── 📄 tr25.md
│       ├── 📄 tr250.md
│       ├── 📄 tr251.md
│       ├── 📄 tr252.md
│       ├── 📄 tr253.md
│       ├── 📄 tr254.md
│       ├── 📄 tr255.md
│       ├── 📄 tr256.md
│       ├── 📄 tr257.md
│       ├── 📄 tr258.md
│       ├── 📄 tr259.md
│       ├── 📄 tr26.md
│       ├── 📄 tr260.md
│       ├── 📄 tr261.md
│       ├── 📄 tr262.md
│       ├── 📄 tr263.md
│       ├── 📄 tr264.md
│       ├── 📄 tr265.md
│       ├── 📄 tr266.md
│       ├── 📄 tr267.md
│       ├── 📄 tr268.md
│       ├── 📄 tr269.md
│       ├── 📄 tr27.md
│       ├── 📄 tr270.md
│       ├── 📄 tr271.md
│       ├── 📄 tr272.md
│       ├── 📄 tr273.md
│       ├── 📄 tr274.md
│       ├── 📄 tr275.md
│       ├── 📄 tr276.md
│       ├── 📄 tr277.md
│       ├── 📄 tr278.md
│       ├── 📄 tr279.md
│       ├── 📄 tr28.md
│       ├── 📄 tr280.md
│       ├── 📄 tr281.md
│       ├── 📄 tr282.md
│       ├── 📄 tr283.md
│       ├── 📄 tr284.md
│       ├── 📄 tr285.md
│       ├── 📄 tr286.md
│       ├── 📄 tr287.md
│       ├── 📄 tr288.md
│       ├── 📄 tr289.md
│       ├── 📄 tr29.md
│       ├── 📄 tr290.md
│       ├── 📄 tr291.md
│       ├── 📄 tr292.md
│       ├── 📄 tr293.md
│       ├── 📄 tr294.md
│       ├── 📄 tr295.md
│       ├── 📄 tr296.md
│       ├── 📄 tr297.md
│       ├── 📄 tr298.md
│       ├── 📄 tr299.md
│       ├── 📄 tr3.md
│       ├── 📄 tr30.md
│       ├── 📄 tr300.md
│       ├── 📄 tr301.md
│       ├── 📄 tr302.md
│       ├── 📄 tr303.md
│       ├── 📄 tr304.md
│       ├── 📄 tr305.md
│       ├── 📄 tr306.md
│       ├── 📄 tr307.md
│       ├── 📄 tr308.md
│       ├── 📄 tr309.md
│       ├── 📄 tr31.md
│       ├── 📄 tr310.md
│       ├── 📄 tr311.md
│       ├── 📄 tr312.md
│       ├── 📄 tr313.md
│       ├── 📄 tr314.md
│       ├── 📄 tr315.md
│       ├── 📄 tr316.md
│       ├── 📄 tr317.md
│       ├── 📄 tr318.md
│       ├── 📄 tr319.md
│       ├── 📄 tr32.md
│       ├── 📄 tr320.md
│       ├── 📄 tr321.md
│       ├── 📄 tr322.md
│       ├── 📄 tr323.md
│       ├── 📄 tr324.md
│       ├── 📄 tr325.md
│       ├── 📄 tr326.md
│       ├── 📄 tr327.md
│       ├── 📄 tr328.md
│       ├── 📄 tr329.md
│       ├── 📄 tr33.md
│       ├── 📄 tr330.md
│       ├── 📄 tr331.md
│       ├── 📄 tr332.md
│       ├── 📄 tr333.md
│       ├── 📄 tr334.md
│       ├── 📄 tr335.md
│       ├── 📄 tr336.md
│       ├── 📄 tr337.md
│       ├── 📄 tr338.md
│       ├── 📄 tr339.md
│       ├── 📄 tr34.md
│       ├── 📄 tr340.md
│       ├── 📄 tr341.md
│       ├── 📄 tr342.md
│       ├── 📄 tr343.md
│       ├── 📄 tr344.md
│       ├── 📄 tr345.md
│       ├── 📄 tr346.md
│       ├── 📄 tr347.md
│       ├── 📄 tr348.md
│       ├── 📄 tr349.md
│       ├── 📄 tr35.md
│       ├── 📄 tr350.md
│       ├── 📄 tr351.md
│       ├── 📄 tr352.md
│       ├── 📄 tr353.md
│       ├── 📄 tr354.md
│       ├── 📄 tr355.md
│       ├── 📄 tr356.md
│       ├── 📄 tr357.md
│       ├── 📄 tr358.md
│       ├── 📄 tr359.md
│       ├── 📄 tr36.md
│       ├── 📄 tr360.md
│       ├── 📄 tr361.md
│       ├── 📄 tr362.md
│       ├── 📄 tr363.md
│       ├── 📄 tr364.md
│       ├── 📄 tr365.md
│       ├── 📄 tr366.md
│       ├── 📄 tr367.md
│       ├── 📄 tr368.md
│       ├── 📄 tr369.md
│       ├── 📄 tr37.md
│       ├── 📄 tr370.md
│       ├── 📄 tr371.md
│       ├── 📄 tr372.md
│       ├── 📄 tr373.md
│       ├── 📄 tr374.md
│       ├── 📄 tr375.md
│       ├── 📄 tr376.md
│       ├── 📄 tr377.md
│       ├── 📄 tr378.md
│       ├── 📄 tr379.md
│       ├── 📄 tr38.md
│       ├── 📄 tr380.md
│       ├── 📄 tr381.md
│       ├── 📄 tr382.md
│       ├── 📄 tr383.md
│       ├── 📄 tr384.md
│       ├── 📄 tr385.md
│       ├── 📄 tr386.md
│       ├── 📄 tr387.md
│       ├── 📄 tr388.md
│       ├── 📄 tr389.md
│       ├── 📄 tr39.md
│       ├── 📄 tr390.md
│       ├── 📄 tr391.md
│       ├── 📄 tr392.md
│       ├── 📄 tr393.md
│       ├── 📄 tr394.md
│       ├── 📄 tr395.md
│       ├── 📄 tr396.md
│       ├── 📄 tr397.md
│       ├── 📄 tr398.md
│       ├── 📄 tr399.md
│       ├── 📄 tr4.md
│       ├── 📄 tr40.md
│       ├── 📄 tr400.md
│       ├── 📄 tr401.md
│       ├── 📄 tr402.md
│       ├── 📄 tr403.md
│       ├── 📄 tr404.md
│       ├── 📄 tr405.md
│       ├── 📄 tr406.md
│       ├── 📄 tr407.md
│       ├── 📄 tr408.md
│       ├── 📄 tr409.md
│       ├── 📄 tr41.md
│       ├── 📄 tr410.md
│       ├── 📄 tr411.md
│       ├── 📄 tr412.md
│       ├── 📄 tr413.md
│       ├── 📄 tr414.md
│       ├── 📄 tr415.md
│       ├── 📄 tr416.md
│       ├── 📄 tr417.md
│       ├── 📄 tr418.md
│       ├── 📄 tr419.md
│       ├── 📄 tr42.md
│       ├── 📄 tr420.md
│       ├── 📄 tr421.md
│       ├── 📄 tr422.md
│       ├── 📄 tr423.md
│       ├── 📄 tr424.md
│       ├── 📄 tr425.md
│       ├── 📄 tr426.md
│       ├── 📄 tr427.md
│       ├── 📄 tr428.md
│       ├── 📄 tr429.md
│       ├── 📄 tr43.md
│       ├── 📄 tr430.md
│       ├── 📄 tr431.md
│       ├── 📄 tr432.md
│       ├── 📄 tr433.md
│       ├── 📄 tr434.md
│       ├── 📄 tr435.md
│       ├── 📄 tr436.md
│       ├── 📄 tr437.md
│       ├── 📄 tr438.md
│       ├── 📄 tr439.md
│       ├── 📄 tr44.md
│       ├── 📄 tr440.md
│       ├── 📄 tr441.md
│       ├── 📄 tr442.md
│       ├── 📄 tr443.md
│       ├── 📄 tr444.md
│       ├── 📄 tr445.md
│       ├── 📄 tr446.md
│       ├── 📄 tr447.md
│       ├── 📄 tr448.md
│       ├── 📄 tr449.md
│       ├── 📄 tr45.md
│       ├── 📄 tr450.md
│       ├── 📄 tr451.md
│       ├── 📄 tr452.md
│       ├── 📄 tr453.md
│       ├── 📄 tr454.md
│       ├── 📄 tr455.md
│       ├── 📄 tr456.md
│       ├── 📄 tr457.md
│       ├── 📄 tr458.md
│       ├── 📄 tr459.md
│       ├── 📄 tr46.md
│       ├── 📄 tr460.md
│       ├── 📄 tr461.md
│       ├── 📄 tr462.md
│       ├── 📄 tr463.md
│       ├── 📄 tr464.md
│       ├── 📄 tr465.md
│       ├── 📄 tr466.md
│       ├── 📄 tr467.md
│       ├── 📄 tr468.md
│       ├── 📄 tr469.md
│       ├── 📄 tr47.md
│       ├── 📄 tr470.md
│       ├── 📄 tr471.md
│       ├── 📄 tr472.md
│       ├── 📄 tr473.md
│       ├── 📄 tr474.md
│       ├── 📄 tr475.md
│       ├── 📄 tr476.md
│       ├── 📄 tr477.md
│       ├── 📄 tr478.md
│       ├── 📄 tr479.md
│       ├── 📄 tr48.md
│       ├── 📄 tr480.md
│       ├── 📄 tr481.md
│       ├── 📄 tr482.md
│       ├── 📄 tr483.md
│       ├── 📄 tr484.md
│       ├── 📄 tr485.md
│       ├── 📄 tr486.md
│       ├── 📄 tr487.md
│       ├── 📄 tr488.md
│       ├── 📄 tr489.md
│       ├── 📄 tr49.md
│       ├── 📄 tr490.md
│       ├── 📄 tr491.md
│       ├── 📄 tr492.md
│       ├── 📄 tr493.md
│       ├── 📄 tr494.md
│       ├── 📄 tr495.md
│       ├── 📄 tr496.md
│       ├── 📄 tr5.md
│       ├── 📄 tr50.md
│       ├── 📄 tr51.md
│       ├── 📄 tr52.md
│       ├── 📄 tr53.md
│       ├── 📄 tr54.md
│       ├── 📄 tr55.md
│       ├── 📄 tr56.md
│       ├── 📄 tr57.md
│       ├── 📄 tr58.md
│       ├── 📄 tr59.md
│       ├── 📄 tr6.md
│       ├── 📄 tr60.md
│       ├── 📄 tr61.md
│       ├── 📄 tr62.md
│       ├── 📄 tr63.md
│       ├── 📄 tr64.md
│       ├── 📄 tr65.md
│       ├── 📄 tr66.md
│       ├── 📄 tr67.md
│       ├── 📄 tr68.md
│       ├── 📄 tr69.md
│       ├── 📄 tr7.md
│       ├── 📄 tr70.md
│       ├── 📄 tr71.md
│       ├── 📄 tr72.md
│       ├── 📄 tr73.md
│       ├── 📄 tr74.md
│       ├── 📄 tr75.md
│       ├── 📄 tr76.md
│       ├── 📄 tr77.md
│       ├── 📄 tr78.md
│       ├── 📄 tr79.md
│       ├── 📄 tr8.md
│       ├── 📄 tr80.md
│       ├── 📄 tr81.md
│       ├── 📄 tr82.md
│       ├── 📄 tr83.md
│       ├── 📄 tr84.md
│       ├── 📄 tr85.md
│       ├── 📄 tr86.md
│       ├── 📄 tr87.md
│       ├── 📄 tr88.md
│       ├── 📄 tr89.md
│       ├── 📄 tr9.md
│       ├── 📄 tr90.md
│       ├── 📄 tr91.md
│       ├── 📄 tr92.md
│       ├── 📄 tr93.md
│       ├── 📄 tr94.md
│       ├── 📄 tr95.md
│       ├── 📄 tr96.md
│       ├── 📄 tr97.md
│       ├── 📄 tr98.md
│       └── 📄 tr99.md
├── 📁 docs/
│   ├── 📄 ai_coding_instructions.md
│   ├── 📄 design.md
│   ├── 📄 development_environment.md
│   ├── 📄 GDSC API Documentation.md
│   ├── 📄 learning_log.md
│   ├── 📄 pocketflow.md
│   └── 📄 terminal_training.md
├── 📁 notebooks/
│   └── 📄 01_data_exploration.ipynb.ipynb
├── 📁 pocketflow/
│   ├── 📁 __pycache__/
│   │   └── 📄 __init__.cpython-312.pyc
│   ├── 🐍 __init__.py
│   └── 📄 __init__.pyi
├── 📁 src/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-310.pyc
│   │   └── 📄 __init__.cpython-312.pyc
│   ├── 📁 utils/
│   │   ├── 📁 __pycache__/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 call_llm.py
│   │   ├── 🐍 data_retrieval.py
│   │   ├── 🐍 gdsc_utils.py
│   │   └── 🐍 s3_helper.py
│   ├── 🐍 __init__.py
│   ├── 🐍 flow.py
│   └── 🐍 nodes.py
├── 📁 tests/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-310.pyc
│   │   ├── 📄 __init__.cpython-312.pyc
│   │   ├── 📄 test_call_llm.cpython-310-pytest-8.4.2.pyc
│   │   ├── 📄 test_call_llm.cpython-312-pytest-8.4.2.pyc
│   │   ├── 📄 test_call_mistral_real.cpython-312-pytest-8.4.2.pyc
│   │   ├── 📄 test_integration.cpython-312-pytest-8.4.2.pyc
│   │   ├── 📄 test_matching.cpython-312-pytest-8.4.2.pyc
│   │   ├── 📄 test_nodes.cpython-312-pytest-8.4.2.pyc
│   │   └── 📄 test_utils.cpython-312-pytest-8.4.2.pyc
│   ├── 🐍 __init__.py
│   ├── 🐍 test_call_llm.py
│   ├── 🐍 test_integration.py
│   ├── 🐍 test_matching.py
│   ├── 🐍 test_nodes.py
│   └── 🐍 test_utils.py
├── 📄 codebase_documentation.md
├── 🐍 collect_python_codebase_info.py
├── 🐍 collect_python_codebase_info_v2.py
├── 📄 condensed_codebase_doc.md
├── 🐍 generic_s3_downloader.py
├── 📄 LICENSE
├── 📄 pyproject.toml
├── 📄 README.md
├── 📄 run_startup.sh
├── 📄 test_notebook.ipynb
└── 📄 uv.lock
```

---

## 📑 Table of Contents

1. [green-agent-age-of-inference-ii/collect_python_codebase_info.py](#green-agent-age-of-inference-ii-collect_python_codebase_info-py)
2. [green-agent-age-of-inference-ii/collect_python_codebase_info_v2.py](#green-agent-age-of-inference-ii-collect_python_codebase_info_v2-py)
3. [green-agent-age-of-inference-ii/generic_s3_downloader.py](#green-agent-age-of-inference-ii-generic_s3_downloader-py)
4. [green-agent-age-of-inference-ii/pocketflow/__init__.py](#green-agent-age-of-inference-ii-pocketflow-__init__-py)
5. [green-agent-age-of-inference-ii/src/__init__.py](#green-agent-age-of-inference-ii-src-__init__-py)
6. [green-agent-age-of-inference-ii/src/flow.py](#green-agent-age-of-inference-ii-src-flow-py)
7. [green-agent-age-of-inference-ii/src/nodes.py](#green-agent-age-of-inference-ii-src-nodes-py)
8. [green-agent-age-of-inference-ii/src/utils/__init__.py](#green-agent-age-of-inference-ii-src-utils-__init__-py)
9. [green-agent-age-of-inference-ii/src/utils/call_llm.py](#green-agent-age-of-inference-ii-src-utils-call_llm-py)
10. [green-agent-age-of-inference-ii/src/utils/data_retrieval.py](#green-agent-age-of-inference-ii-src-utils-data_retrieval-py)
11. [green-agent-age-of-inference-ii/src/utils/gdsc_utils.py](#green-agent-age-of-inference-ii-src-utils-gdsc_utils-py)
12. [green-agent-age-of-inference-ii/src/utils/s3_helper.py](#green-agent-age-of-inference-ii-src-utils-s3_helper-py)
13. [green-agent-age-of-inference-ii/tests/__init__.py](#green-agent-age-of-inference-ii-tests-__init__-py)
14. [green-agent-age-of-inference-ii/tests/test_call_llm.py](#green-agent-age-of-inference-ii-tests-test_call_llm-py)
15. [green-agent-age-of-inference-ii/tests/test_integration.py](#green-agent-age-of-inference-ii-tests-test_integration-py)
16. [green-agent-age-of-inference-ii/tests/test_matching.py](#green-agent-age-of-inference-ii-tests-test_matching-py)
17. [green-agent-age-of-inference-ii/tests/test_nodes.py](#green-agent-age-of-inference-ii-tests-test_nodes-py)
18. [green-agent-age-of-inference-ii/tests/test_utils.py](#green-agent-age-of-inference-ii-tests-test_utils-py)

---

## 📄 Source Files

### <a name="green-agent-age-of-inference-ii-collect_python_codebase_info-py"></a>green-agent-age-of-inference-ii/collect_python_codebase_info.py

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-collect_python_codebase_info_v2-py"></a>green-agent-age-of-inference-ii/collect_python_codebase_info_v2.py

> 💬 **Developer Note:** The python script which was used to generate this documentation.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-generic_s3_downloader-py"></a>green-agent-age-of-inference-ii/generic_s3_downloader.py

> 💬 **Developer Note:** Downloads all files from a specified S3 prefix to a local directory. Currently the data is already in the environment.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-pocketflow-__init__-py"></a>green-agent-age-of-inference-ii/pocketflow/__init__.py

> 💬 **Developer Note:** The main framework of the application core architecture. It's amazing that entire framework is only 100-lines of python code.

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

> 💬 **Developer Note:** This is empty file which is comman python convention to make the directory as Python Package which then can be imported elsewhere.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-flow-py"></a>green-agent-age-of-inference-ii/src/flow.py

> 💬 **Developer Note:** Currently empty, this is where the flow logic will be implemented.

**Size:** 0 bytes

```python

```

---

### <a name="green-agent-age-of-inference-ii-src-nodes-py"></a>green-agent-age-of-inference-ii/src/nodes.py

> 💬 **Developer Note:** Currently empty, this is where various nodes will be defined.

**Size:** 0 bytes

```python

```

---

### <a name="green-agent-age-of-inference-ii-src-utils-__init__-py"></a>green-agent-age-of-inference-ii/src/utils/__init__.py

> 💬 **Developer Note:** This is empty file which is comman python convention to make the directory as Python Package which then can be imported elsewhere.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-utils-call_llm-py"></a>green-agent-age-of-inference-ii/src/utils/call_llm.py

> 💬 **Developer Note:** Contains utility function for calling LLM. This is the component that makes an AI application as and AI application.

**Size:** 5272 bytes

```python
import os
import logging
from functools import lru_cache
from mistralai import Mistral
from typing import List, Dict, Optional

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Internal cached function ---
@lru_cache(maxsize=128)
def _cached_mistral_call(model: str, messages_tuple: tuple) -> str:
    """
    Internal function that performs the actual API call.
    Caching is applied here. Messages are converted to a tuple to be hashable.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        logger.error("Cannot call Mistral API, MISTRAL_API_KEY is not set.")
        raise ValueError("MISTRAL_API_KEY environment variable not found.")
        
    client = Mistral(api_key=api_key)
    
    # --- FIX: Correctly reconstruct the list of dictionaries from the tuple ---
    # The input `messages_tuple` looks like: ((('role', 'user'), ('content', '...')),)
    # We need to convert it back to: [{'role': 'user', 'content': '...'}]
    messages_list = [dict(msg_tuple) for msg_tuple in messages_tuple]
    # --------------------------------------------------------------------------
    
    logger.info(f"Making a LIVE API call to model: {model}...")
    response = client.chat.complete(
        model=model,
        messages=messages_list
    )
    return response.choices[0].message.content

# --- Main utility function for external use ---
def call_llm(
    prompt: Optional[str] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    model: str = "mistral-small-latest",
    use_cache: bool = True
) -> str:
    """
    A robust wrapper for making calls to the Mistral API.

    This function handles chat history, caching, and retries as per Agentic Coding guidelines.

    Args:
        prompt (Optional[str]): A single user prompt. If provided, it overrides `messages`.
        messages (Optional[List[Dict[str, str]]]): A list of messages for chat history.
        model (str): The Mistral model to use. Defaults to "mistral-small-latest".
        use_cache (bool): If True, returns a cached result for the same request.
                          Should be set to `self.cur_retry == 0` within a PocketFlow Node's
                          `exec` method to avoid getting stale results on retries.

    Returns:
        str: The content of the LLM's response.
    
    Raises:
        ValueError: If neither `prompt` nor `messages` are provided, or if the API key is missing.
    """
    if prompt:
        messages_payload = [{"role": "user", "content": prompt}]
    elif messages:
        messages_payload = messages
    else:
        raise ValueError("You must provide either a 'prompt' or 'messages'.")

    try:
        # Convert the list of dictionaries to a tuple of tuples of items to make it hashable
        messages_tuple = tuple(tuple(item.items()) for item in messages_payload)
        
        if use_cache:
            logger.info("Cache is enabled. Checking for a cached response...")
            return _cached_mistral_call(model, messages_tuple)
        else:
            logger.info("Cache is disabled. Forcing a fresh API call...")
            # Use __wrapped__ to bypass the cache of the decorated function
            return _cached_mistral_call.__wrapped__(model, messages_tuple)
            
    except Exception as e:
        logger.error(f"Mistral API call failed: {e}", exc_info=True)
        # Re-raise the exception so the caller (e.g., a PocketFlow Node) can handle it
        raise

# --- Self-testing block ---
if __name__ == '__main__':
    # Ensure you have a .env file with MISTRAL_API_KEY in the project root
    from dotenv import load_dotenv
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        logger.info(f"Loaded environment variables from: {env_path}")

    if not os.getenv("MISTRAL_API_KEY"):
        logger.error("FATAL: MISTRAL_API_KEY not found. Please create a .env file in the project root.")
    else:
        logger.info("--- Running Self-Test for call_llm utility ---")
        test_prompt = "What is a 'green job' in Brazil? Keep it short and practical."

        # 1. First call - should be a LIVE call
        print("\n--- Test 1: First call (cache enabled, but no entry exists) ---")
        response1 = call_llm(prompt=test_prompt, use_cache=True)
        print(f"Response 1:\n{response1}")

        # 2. Second call with cache enabled - should be INSTANT and cached
        print("\n--- Test 2: Second call (with cache, should be a HIT) ---")
        response2 = call_llm(prompt=test_prompt, use_cache=True)
        print(f"Response 2:\n{response2}")
        
        # 3. Third call with same prompt but cache disabled - should be a LIVE call again
        print("\n--- Test 3: Third call (no cache again) ---")
        response3 = call_llm(prompt=test_prompt, use_cache=False)
        print(f"Response 3:\n{response3}")

        print("\n--- Self-Test Complete ---")
```

---

### <a name="green-agent-age-of-inference-ii-src-utils-data_retrieval-py"></a>green-agent-age-of-inference-ii/src/utils/data_retrieval.py

> 💬 **Developer Note:** Currently Empty

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-src-utils-gdsc_utils-py"></a>green-agent-age-of-inference-ii/src/utils/gdsc_utils.py

> 💬 **Developer Note:** This is official utils file given by the GDSC organisers. Currently I'm working on my personal AWS account but I'll pull all the code using `git pull ...`. There are lot of useful utility function that can be used directly or remolded.

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

### <a name="green-agent-age-of-inference-ii-src-utils-s3_helper-py"></a>green-agent-age-of-inference-ii/src/utils/s3_helper.py

> 💬 **Developer Note:** A helper class for common Amazon S3 operations. Provides methods to list, upload, and download objects from S3 buckets,

**Size:** 7824 bytes

```python
import boto3
import logging
from botocore.exceptions import ClientError
from typing import List, Dict, Any, Optional
import os
import shutil # <-- IMPORT SHUTIL for robust cleanup

# --- FIX: Moved logger configuration to the top level ---
# Configure logging for the module
logger = logging.getLogger(__name__)
# Ensure logger has handlers (important for notebooks or standalone scripts)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
# ---------------------------------------------------------

class S3Helper:
    """
    A helper class for common Amazon S3 operations.

    Provides methods to list, upload, and download objects from S3 buckets,
    with improved error handling, logging, and flexibility.
    """

    def __init__(self, region_name: Optional[str] = None):
        """
        Initializes the S3Helper with a Boto3 S3 client.

        Args:
            region_name (Optional[str]): The AWS region to use for the S3 client.
                                         If None, Boto3's default region resolution
                                         (e.g., from environment variables, config files)
                                         will be used.
        """
        if region_name:
            self.s3_client = boto3.client('s3', region_name=region_name)
            logger.info(f"S3Helper initialized for region: {region_name}")
        else:
            self.s3_client = boto3.client('s3')
            logger.info("S3Helper initialized using default region resolution.")

    def list_objects(self, bucket_name: str) -> List[Dict[str, Any]]:
        """
        Lists objects within a specified S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, where each dictionary
                                  contains 'Key' (object key) and 'LastModified'
                                  (creation/last modified time) for each object.
                                  Returns an empty list if no objects are found
                                  or an error occurs.
        """
        objects_info = []
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)

            if 'Contents' in response:
                for obj in response['Contents']:
                    objects_info.append({
                        'Key': obj['Key'],
                        'LastModified': obj['LastModified']
                    })
                logger.info(f"Found {len(objects_info)} objects in bucket: {bucket_name}")
            else:
                logger.info(f"No objects found in bucket: {bucket_name}")
    
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                logger.error(f"Bucket '{bucket_name}' does not exist.")
            else:
                logger.error(f"Client error listing objects in '{bucket_name}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error listing objects in '{bucket_name}': {e}", exc_info=True)
            
        return objects_info

    def upload_file(self, local_file_path: str, bucket_name: str, s3_object_key: str) -> bool:
        """
        Uploads a file from a local path to an S3 bucket.

        Args:
            local_file_path (str): The local path to the file to upload.
            bucket_name (str): The name of the target S3 bucket.
            s3_object_key (str): The desired key (path) for the object in S3.

        Returns:
            bool: True if the file was uploaded successfully, False otherwise.
        """
        if not os.path.exists(local_file_path):
            logger.error(f"Local file '{local_file_path}' not found.")
            return False

        try:
            self.s3_client.upload_file(local_file_path, bucket_name, s3_object_key)
            logger.info(f"File '{local_file_path}' uploaded to '{bucket_name}/{s3_object_key}'")
            return True
        except ClientError as e:
            logger.error(f"Client error uploading '{local_file_path}' to '{bucket_name}/{s3_object_key}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error uploading '{local_file_path}' to '{bucket_name}/{s3_object_key}': {e}", exc_info=True)
        return False
            
    def download_object(self, bucket_name: str, s3_object_key: str, local_file_path: str) -> bool:
        """
        Downloads an object from an S3 bucket to a local file path.

        Args:
            bucket_name (str): The name of the S3 bucket.
            s3_object_key (str): The key (path) of the object in S3.
            local_file_path (str): The desired local path to save the downloaded file.

        Returns:
            bool: True if the object was downloaded successfully, False otherwise.
        """
        try:
            # Ensure the directory for local_file_path exists
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            
            self.s3_client.download_file(bucket_name, s3_object_key, local_file_path)
            logger.info(f"Object '{s3_object_key}' downloaded from '{bucket_name}' to '{local_file_path}'")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logger.error(f"Object '{s3_object_key}' not found in bucket '{bucket_name}'.")
            else:
                logger.error(f"Client error downloading '{s3_object_key}' from '{bucket_name}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error downloading '{s3_object_key}' from '{bucket_name}': {e}", exc_info=True)
        return False

# --- NEW: Self-testing and usage example block ---
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # This is an example bucket. Replace with a real one for testing.
    # NOTE: Ensure your SageMaker execution role has permissions for this bucket.
    TEST_BUCKET = "age-of-inference-ii-dataset" 
    
    print(f"--- Running S3Helper Self-Test against bucket: {TEST_BUCKET} ---")
    
    helper = S3Helper()
    
    print("\n1. Testing: list_objects()")
    objects = helper.list_objects(TEST_BUCKET)
    if objects:
        print(f"✅ SUCCESS: Found {len(objects)} objects. Sample object key: '{objects[0]['Key']}'")
    else:
        print("⚠️ WARNING: Test finished, but no objects were found or an error occurred.")
    
    print("\n2. Testing: download_object() (Example)")
    if objects:
        sample_key = next((obj['Key'] for obj in objects if not obj['Key'].endswith('/')), None)
        
        if sample_key:
            temp_dir = "temp_s3_test"
            local_path = os.path.join(temp_dir, sample_key)
            
            print(f"Attempting to download '{sample_key}' to '{local_path}'...")
    
            success = helper.download_object(TEST_BUCKET, sample_key, local_path)
            if success and os.path.exists(local_path):
                print(f"✅ SUCCESS: File downloaded successfully.")
                # --- FIX: Use shutil.rmtree for robust cleanup ---
                print(f"Cleaning up temporary directory: {temp_dir}")
                shutil.rmtree(temp_dir)
                # --------------------------------------------------
            else:
                print("❌ FAILED: Download test failed. Check logs.")
        else:
            print("Skipping download test as no file objects were found (only directories).")
    
    print("\n--- Self-Test Complete ---")
```

---

### <a name="green-agent-age-of-inference-ii-tests-__init__-py"></a>green-agent-age-of-inference-ii/tests/__init__.py

> 💬 **Developer Note:** This is empty __init__.py file for the tests directory. We'll use TDD religiously and we're using `pytest`.

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_call_llm-py"></a>green-agent-age-of-inference-ii/tests/test_call_llm.py

> 💬 **Developer Note:** Test for call_llm utility python script.

**Size:** 2239 bytes

```python
import pytest
import os
from src.utils.call_llm import call_llm
from dotenv import load_dotenv

_ = load_dotenv()

# --- Marker to check if the MISTRAL_API_KEY is available ---
# The test will be skipped if the API key is not found in the environment variables.
# This prevents test failures in CI/CD or other environments without the key.
requires_mistral_api_key = pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="This test requires the MISTRAL_API_KEY environment variable to be set."
)

@requires_mistral_api_key
def test_call_llm_with_api_key_returns_string_response():
    """
    Tests that a call to the Mistral API with a valid key and prompt
    returns a non-empty string response.
    
    This test makes a real, live API call.
    """
    # Arrange
    test_prompt = "What are the three most common renewable energy sources?"
    
    # Act
    # We call with use_cache=False to ensure the test always hits the live API
    response = call_llm(prompt=test_prompt, use_cache=False)
    
    # Assert
    assert isinstance(response, str), "The response should be a string."
    assert len(response) > 0, "The response string should not be empty."
    print(f"Response: \n{response}")
    print(f"\nLive API test successful. Received response of {len(response)} characters.")

def test_call_llm_without_prompt_or_messages_raises_error():
    """
    Tests that the call_llm function raises a ValueError if no input is provided.
    """
    # Arrange, Act, Assert
    with pytest.raises(ValueError, match="You must provide either a 'prompt' or 'messages'."):
        call_llm()

def test_call_llm_without_api_key_raises_error(monkeypatch):
    """
    Tests that the call_llm function raises a ValueError if the API key is missing.
    We use monkeypatch to temporarily remove the environment variable for this test.
    """
    # Arrange
    # Temporarily remove the API key from the environment for the duration of this test
    if "MISTRAL_API_KEY" in os.environ:
        monkeypatch.delenv("MISTRAL_API_KEY")
    
    test_prompt = "This should fail."
    
    # Act, Assert
    with pytest.raises(ValueError, match="MISTRAL_API_KEY environment variable not found."):
        call_llm(prompt=test_prompt)
```

---

### <a name="green-agent-age-of-inference-ii-tests-test_integration-py"></a>green-agent-age-of-inference-ii/tests/test_integration.py

> 💬 **Developer Note:** Currently Empty

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_matching-py"></a>green-agent-age-of-inference-ii/tests/test_matching.py

> 💬 **Developer Note:** Currently Empty

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_nodes-py"></a>green-agent-age-of-inference-ii/tests/test_nodes.py

> 💬 **Developer Note:** Currently Empty

*File content intentionally excluded by user.*

---

### <a name="green-agent-age-of-inference-ii-tests-test_utils-py"></a>green-agent-age-of-inference-ii/tests/test_utils.py

> 💬 **Developer Note:** Currently empty

*File content intentionally excluded by user.*

---

