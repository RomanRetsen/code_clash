"""
Cargo trucks are transporting containers due for export to a seaport terminal.

The containers will be temporarily stored in the terminal to wait for ships to come. To save space, containers are usually stacked up in the terminal.

There are different ships bound for different destinations. Terminal operators have to pick the correct containers from temporary storage to load onto the ships. If the correct containers are on the top of the stack, it will be easy to pick them up for loading. But if a wanted container is underneath some other containers, the overlaying containers must first be moved aside before reaching the wanted container, causing extra operation cost and wasting time.

To manage the container terminal in the most efficient manner, you need a plan.

There are ship A to ship Z, totally 26 different ships bound for 26 different destinations.

You know the schedule of the ships. Ship A will come earlier than Ship B. Ship B will come earlier than Ship C. The ships always come in alphabetical order.

You know the schedule of the cargo trucks. The containers for different ships are arriving in a predictable order. No cargo owner wishes to miss a shipment. All cargoes will arrive before the first ship to come.

You have to plan when the trucks come, how should the containers be stored.

Example

Six trucks are sending six containers to the terminal in this order:

BACCBA


B is a container for ship B. This container comes first.
It is followed by container A, targeted for ship A.
A is followed by two containers C, to be loaded to ship C.
... and so on for the rest.

We can arrange the six containers in two stacks, like this:

 ___ ___
| A | B |
|___|___|
| A | C |
|___|___|
| B | C |
|___|___|


When ship A comes, we can pick up the two uppermost A containers to load to the ship.
When ship B comes, the two B containers are on the uppermost layer easy to pick up.
When ship C comes, the remaining two C containers are ready for pick up and loading.

The whole process used 2 stacking areas.

Note that we do not sort the containers before stacking them up. Sorting is an option too slow and costly to put in practice.

Now is your turn. You will have the cargo trucks schedule. You know ships are always arriving in alphabetical order. Find the minimum stacking areas needed to ensure the most efficient shipment loading.
Input
Line 1: An integer N for the number of lines to follow.
The following N lines: each line is an independent test case, which is a string composed of alphabetical upper case letters. Each letter refers to a container targeted for its same-letter ship. The cargoes will be transported to the terminal strictly in the order shown in the string. Process each line as an independent case.
Output
Write N lines, each line is an integer, which is the answer for its corresponding input line.
Constraints
1 ≤ N ≤ 100
1 ≤ length of each line ≤ 500 characters

In the real world there is a maximum height limit for each stack of containers. In this puzzle we assume there is no such limit.
Example

-----------test1
Input

5
A
CBACBACBACBACBACBA
CCCCCBBBBBAAAAA
BDNIDPD
CODINGAME

Output

1
3
1
4
4
-----------test2

15
C
JS
VB
CPP
PHP
JAVA
PERL
RUBY
MYSQL
PYTHON
GROOVY
PASCAL
POSTGRES
HIBERNATE
KUBERNETES

output

1
2
1
2
2
2
2
3
2
2
4
3
3
4
4


-----------test3

30
L
CBB
XXTX
TMDNU
OOOOO
DTUUTT
ENEENL
KOKKKOKK
EQJCCQQQ
NNNNNNNNN
LLLLLLLLLL
JNFAEGMCEWC
BBBPBBPPPPPB
VVVMVTFMHHMM
WRARVTRANRAW
MQLNLQLLQMLNLON
GELGGLSTWZEHCHGLG
MIWEWESTEWEMEMIMEW
JJBYHJRHJYZQHWWTBBHB
WNYRNRYRRRNYNYFDRFRNF
OZSYFMSSZLQOFPFCLFLEWCA
HHJXJJXHXXXHHHJXJXHHXHJH
NNFNNUXQWWXTGHWDSFHQTJDGN
WOTDRNAYBWISURBXVMBFQJHEPO
ZEMAROWQMECRUOWUPEWMOORMAREP
CMMNOOVOSNVMNCCCVCICSMCMIVVI
ZILJCMABQPNLMLIEEAAEBQMVCPIZJB
JXFFXLXFFFFFFSCXXFJCCSXSFFFJFX
SSSKMSPKPPPMKKMMPMSPPKKSSSMPKMPM
FHSDNARRCTCRNARSTDRHRHAHDSNFDFFHNCAT

output

1
1
2
3
1
3
2
2
3
1
1
5
2
3
4
4
7
4
6
3
5
3
5
6
7
6
7
5
4
7

-------------test4

30
RCCMBQZDGNKCPCRNYBRFQPNZKGOBSFYWDNZYMVSBCSBHIBIRCVORNBWQGVQIGCMCTQNRRIWIYFSCOBSKDKVSWYODPWHYZCDQPBHTDOCFHOPKNSZKPGCQWOYYSNBZYFOMKKWZFTFROFDI
ONPYPGPNWOXWUIOMIMYWHSSPLVPLPVPAYPSAHNYMXWASXYUGXXNGXOPUIAMYPSSNSWPHPSPYOUWSUOUXPUVUNIGOOAUUGLVLGYXOIYIHLIUWNSNMNSXVWVNSLPSSASVAAOXOUOGMXHAVHWAAXYVNLW
PVVBPCMFUXVKVILYALPYVCFVPIUKAKMDFPYVUVFUIMILYKDLVVAIDXBBVXDAVBVVIKKIBYFVCVVBLVMDPYAUDMVNPYNPCIFDLUVVKXXPYMMUXKKDBAFFFLAKCKVFCXAYNUUDDPKABDBMXBMAIKDLBN
ZBYFAYFDAWQFSJFOZGGDWJEQQDGFQMZGFDNKKUMKKMJYDOGNOAUJZBQQGWOEGQJSEQMKWWNKYSEZYSZDANYQDMMNMAOJWSEAWESKAKZOASGOYSYENJGSKJDFBBQSUZGBYMJOYDKAKZNQSSQSOZJUMOGMQ
AASLMHXNAWOXLWFYHEEPOXOXMFAYZQQNZBNBAWZRWFFPQRPRHLZWFZAQLEMLHBHRYYMREQSOBYNXYXRHBFWBSHPRAORFWVVLTFMRPSGGZPQPVETWFYTQEAYWHZEZVVHXSFGYSXMMQWEARQLXZEFBPWYAAWLNXNLG
FDWYNMXHTHBSHCTXXSKXSGPBACHNFPKTHWEXIWTCSNYMWYHXSJTWPKTTTAHWPIXBGABCJJAXJCXXBNPFXHGHGAMLSAFSGCKKMNEGIGWIEKEBGHBYKJYTCTKSFPNHTLMKPEBSDDCEEBIISWDGGLJBNHTCBEILSDMW
JEWTOTOGJFEZSWGUOVQGJEZWIXSEJSIFFOOYZSVFSQFOQLIZRFFOUBQILUVXEFTQQKTYLKLVLZZWFTBACECIILEIFJBYKZKUIOKJZQYQYSYVGOLFECJXRSQVSGGIKFBABKKKFQWISAXZAWGBVLSAJKGUOSAIVBCFXEQUZJOY
QLMVXSGRRPRSVXNAQWBVHIMGENPZJWLRNRGLCGIAWVSARJCZUUNUXRNGUMYPSGRWRAUQYIEOOJABOHAOOMHIIDXDVNKUJEBXJUWPMSPLXGOGKNZCBMIKRWPQGAZOWBZJNJNSKOKPISNGYDDLOIQKXDZBCSNJCUPYMQZLNYHZ
MJTYRUPEMWOHTYHHBUNRFFKNMWJLUFJNFAPBBSOFOMPCIZBBHLLRWYGNMWTDPBLYDMHBTBCMUPAJBUGHWOLKJKZBJWXRYOXXSSXUKHIHUOYSKBURMFBHURZGOOHTCMJPNDAWHEWBUYUCZYKNOZBRTTLACBTHJMGZOXIUTFPU
TFRDQTJQTQAWRZHHKFWIEWRQNKNIPFFPHKTHLLJDQRZJKQTQQHRAFRAAARZZNWVJNJWQKNJFJFQDTFQJQJEAIKRTWFFLWLKNVQAQDZIJDFNIINLPVVZDTENALLWPVADFITNAFZKLFLPQEETRDWHEPELIDWJDHWLIZKWWKVZHVP
IEEQGWVWZBZGWBZZTQCFXSPYRXHDBGDBTIYZTFEOHDFFWXOPGRIDZEIXTHEFPROSGGDSVZFFFGFZTIICBYEZVPBOTGGZDXGFWERQOYIVHRBQBFQIOGFDEYTIOGBVOYZXOVPPBWBZGEBDCISWXXPEVYDHGFIPRZFGCTDXWXTVTDR
IJNTFQUAVOWFEJGIGOXRXKEEPVETJKUUWHBOMMASWGMIAXSNDIMVJFRGUDRSUFRRSNDBFWTQUSSNKHWWNGGDBWNGDVVAKBFEQOKHVRIBAVKWOBUMFOKONKHXQGBXTXSEIGGPNNBGFFKAJISTGOUUDNAXAIFHVDNPAIOFBPHNNOJRRVII
XFZXIUABPFWEWVWKAVPRJARYHPPTPNNJDEZIIXBCYABKKHJAPRVPXNFXZQZBKQZVZITPZEIHJAEPBXISAPVYXJKRYWJJUUZHFXNYACQKEAEEJVUZQJSURIEEDNQVEQYVARJHYAFSIJNIBNBVUFUEDCHRVEZVHZTPWJXVYYPVZSSZTQAXFJETDTNJCNWNKYHTPJFVKA
UQAPHCABCNHNEVEQYPSEKZGPEKWWDZCZZCEZJLHJENUSQWLFQGJKNUCEYVYEZUEYCAGUPNKIQZKBZDSENCZVIDVCLSSVPCOWLBHWQZBGNOZJHVSFJSJGCANJPGGOOHEUDENHYIGCWNAJDWALSFASFYSBHJZVCWUBGUEEIENOLNBGVKPPLIVPCAYPVJSZQLEGZYSDZV
ICDIDLTRIZJASAHPUVJBDUNQTGXRJOUKESWENEIAHLANELPDFAJHTXGBOKJBDABMOFCQQPBKNSFWVBLRWGJOMDJBDIEQPHHEIIZZMAXZKCQCLCDJIHWWAMBAQROGSQQVZZZPBKXGSUIFIMZOWIFTXMEORKLNUWAACXRKDELCCOOGVUAIPDABVVZHXDRUAWXPGRTBPQEP
DPKZYYSLCWTQKDLYTTSWPSLBTQCICIBOYSNVPSKRNFANITYKVNYSFZKORINPSGSTWROSVSGPOKTGGKOYQDOIPBLBLTVCQKCCSSAKKDZFSZZFGRDRBDWWVNPCQLQQQOFIGFNRYNOADKWZYPZQFNIRQYCRTKGITIWSLRFRVKTBCPBVGDDBZFINZZSKKKGCOKQSNIOTDFGV
PFTELFHYYFTFVESFXHSJRTYNAESVJAPUWLBHLDFJWFQHRSPAXYNTXHPPBHWAGHMELUALLQMQJBHJXXBLPDMXBKVLMUGXGOOTGRULNHWBEFRUQWOKPHFVLSRHELOONNUKPVDXVGQESNUMXONYHPOYDVUNBLXDOXMXGBJRNWOTRDXOAGPBTJVPPUYHBNAWJHSDHYGBASJOPGOAMOV
CQIJOFOZIFAMXYFIWBWYUCZUDZDBDDMULUBDRXVQUFWYJKAPIRMINKLFDGLGFXVRHJVHOVFOBRXXZLIGFOINQIOJJURQHULZGHPKRYDQHHOHIPVUXUKURKZDMKRKDAFPBIRYRRMPZNGQBFHAWBFKYMWODMCBMXLHRRKRDUKAFJYQRWHLAIXWXCDVDCUXKUHJICUOUHHRHJWCPHV
KYUWCSEYOXYULIDKZAYHYSYUXOYKSISWCELJIEHHKZALINKJJLZFFMOUARSBYXIJVOJNBFBZNDXASSZROENUUDLUZCZSCDCCQEVMRUXQSCWWMLYFMDMZSYLUMKOKEDCSESNHXODSULDZXLVXEFEWAOWHZRNZQOFUKMQILXUNLNRSONADNZDQNMKHASZAJOZXUYWUCEWRFKHCFKX
SXHDIVAJQVHWMRHQSONIHFMSAKPZBABOFOVXMHXSANIHZFHVNVHHADVXMQNZZXLODAHNZOFKXSIWOOWQAIYQMOBHJVVZFBQWDSPIVNVLZLDFVRFIXLJWMXIAWLIILOVJZVNOZNMJAVMIDJMWQPDDHOHPWADSKZVIPRKNRWXBLOXBPDMAIHDKZXFKQQAILLKLBZHZJBDOAAHSBAFKWO
OBOYGWFOWBBTCNLKAFJPNJDDFFMTLQYQMJXOLKMDLNCMTASJYTLNMVKSSJNPORQGDJWXPRWPPCSYABTTJGXROWXQGBYQVYQKRQXGPBTROYQOOQKAQNFYKBJKCQCBCOBAYSBMQFSKRSCPTPQCTOMFKASCDTRNOLSSTTYFMXMFOYJOGFRNTQVNPRWBJTOMGTQQQMDQQYDFYJNCTPCGKT
VBPXTJGKIKWJJBCPVJYRXYIGTIOXIYYKWTJBRIMHQISVHVHCPKJWLHXPPILYGYVTYYVKSTMPWTPYDVDSMMBOLKXIMDPLXUWKXHVTYRMDTOYKQPTRTWMOJVVPDQOPGWMCYDDTYUDTMWHKIWQRIVGJKVVXWDDXBCIWKUBTLDTDIUCVUWUICCSXJUWXHCVXRBTGWTYSXQUUBJGHSDMQBS
CTPGBWNOHVGDTCWWPIWDYBXYGXITMMYLBHPDDLOXTBDBGEXALIVREWWIXDOYLNHXBHMWTHGXRHXBATZMPHGOTOPWNTFYOYWTTENARCTLEBNNCEOBIBOTVTLVWZVRFTBNYLTATZRPONZIOEZMEPINTRLFBNVDRGBFZCFNNETIMGOFXWBZMHRAERZGVNAODHZMIFXMMYPMBVVWGBCIDV
OSXQNNEPVRBIVMGVSRYFLDCYBAGPYCHDZXOMUWROQWEOORXPGGNGBHCGAVCCEALWUCBOGNGLQZDUEHORWAZKIKBANRUAOZMXWZLHOZDEYAEBQBSIBLNLLFFHMPLYPYZQDBADWPHQCVKHHDFCZOORRVMSVGEYVQWRSHGKYZZPUDQXHQCLRIVOSDYVVZOPQLQHCCDGWGHUKBPBDKWVYYAXPUVB
BUILVRRRIEFJYRZQTZFVGPNUUWYLYPNAGJABTPIUWZZLUJZTTPPGKVGBKIEHUYAPHWLXQGFTNEERRZQBPFNVPLQXIMQQXXHLIKMLJIQVXZUQPJQWZDHPUPLRLHURWIMAXHHPMFLJYYUJFAMXPLQRNWXJXTUAMBKGPIPJHPGBRBNQLUVFULYGLAPQTVNBZLEQBKZJDEUJTKZTHTJAFJQGWZKEHDRDHTMFZUWVLX
PDOMUCEOQEVUMMXUJDSNFLMJSKKQIERJXKIGDIFORDJUJPTRUUTOWKJNVCFKFBXDEBJAOOTIANSDEGOFUMEPVETTCNWWQOTIPMPGIVCFDRARIJJWCCVBELMQOUULEVVCUNKRCNPDAQDVWLRFWKTEELNTFOXIJKEAGIMJDDTKCQIOCXILFNILSRIBBDVJGJPSGVPFUBGBRFBREVOIITVFXEFBQGQKKCQUKCPBIX
TZPAIWRTTAUNXIKEBKJPHBUHYSBEEKCVMUBMJXSSDASOUHTNIWYROBSIDDKOPSHRHTTHITYWDCNLHTKSYFNARWRHFPZYYBNDCULFLEFBPZUFNPPJHCSXZPAFYKYUWDDBRTLKUPDDILZDXHSXIYIIWNFLYZRXXWYUTNEMXYKXZKZZAXYSADYNYFPBVXBPJBELOYXFNPMKLDFDITOJBBBZJRLIZKYRCIICDDARBVCESODFJECE
UQXKIMAHCBARYEZCXGCZVMHDGMKDTJWOTFCTMNKFYZNKYACPSQNKVWHFGOZUNVQNNKPFQEGYYTNKSEKZZNKDRCGIIVNYMEIADITDUWPGRCAKTHWIUPIECSTKXBEODIPGJCTWAMBZTAZAUSEDOPCCRFYGDTSIUKHFQHGXOBVCGFIWXPQTKKMJCCGOAUSZHUBXTTSRJPRHEWSVOKNECRUDJYSIQDCWZEZKKORXXGNMZWXNXDGDETMUFUYWRU
TXCQIMAOMNZNTEXAUHXXUDUETWRBTQZKVYOQPYCYEQSCMJJBGMOXTKXAKLONOFHKTWIBJDEBWCECQJWDPHJCBFTUHHHZQBSLDTAXWXZXBOMWHLGMQBMBDPOSESOOOKPXUBVOTHQIWGGDVSXFBOWKDVSLKAFHYBDDGFAROFMDFQPAJQKLILGUNAMLYMBPIUFSWXHSHUDOXOBVSFFRDKSPQYTORPQSCNEEDTUSCHHAONIUPYLVQWUGOIWTELNVAJEDNFHQ
AFVQWZVHOENPVWCTIMHILQNPMEMUIHYLULOCOOEAPUMZHPTABRZLWVBDNMKYVCSIAZGPPIXHBWWJXWFBZXHDITTDUJAPHOICUTJWZWGBXXLCTJYJCNSNBVUDQEPHXCVMFIBXQYFTTGYFIABQZOZYECRRDEUQDRLDRCDIIHHSHNIEPHYXHIKRDRNTFUBDWKIBDCFCKTEVBMWYZTUTABSGYURRXDVRCELKIAESQRHBTHGTZVGKBUZWVHABBQNCQTAWLAZR


output

15
14
14
15
15
15
15
17
14
13
17
15
19
18
19
16
20
17
18
16
18
19
16
19
17
17
17
20
22
19


"""

n = int(input())
for i in range(n):
    line = input()
    the_stacks = [[line[0]], ]
    for container in line[1:]:
        distance_in_alpha = 27
        stack_index = -1
        for index, stack in enumerate(the_stacks):
            if stack[-1] >= container and (ord(stack[-1]) - ord(container)) < distance_in_alpha:
                distance_in_alpha = ord(stack[-1]) - ord(container)
                stack_index = index

        # if none of the stack are good, create new stack
        if stack_index == -1:
            the_stacks.append([container])
        else:
            the_stacks[stack_index].append(container)

    # picking best out of two stacking schemes:
    # 1)creating separate stack for single letter
    # 2)selective stacking 
    print(min(len(the_stacks), len(set(line))))
