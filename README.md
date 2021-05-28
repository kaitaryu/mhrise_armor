# mhrise_armor
There are various types of armor in Monster Hunter Rise, but it is troublesome to think about the combination, so let's ask "cvxpy" to think about the best combination.

2021/05/29 add skill(���C����), add armor(�q�s�m�w����,�q�s�m���C��,�q�s�m�A�[��,�q�s�m�R�C��,�q�s�m�O���[��)

# List of skills you can set up

KO�p,�A�C�e���g�p����,�K�[�h����,�K�[�h���\,�L�m�R��D��,�W�����v�S�l,�X�^�~�i�}����,�X�^�~�i�D��,
�Ђ�݌y��,�t���`���[�W,�{�}�[,�����i�[,���؂̉��b,�Ύ����,�Α����U������,����̉��b,��S���y�����z,
�������UP,��𐫔\,�񕜑��x,��������,�ђʒe�ђʖ��,�C��ϐ�,�S�ΓZ,�t����,�t�P,�|���ߒi�K���,
��������,�ƕ�,���؂�,�K�^,�L�扻,�U�߂̎琨,�U��,�|�k�̉��b,�����ό`,���n����,�U�e�g�U���,�����Ɋ�,
����,��_����,�W��,��,��薼�l,�A���w,�S��,�������U������,������������,�����ϐ�,����̉���,���H��,
���U�g��,���U���x,���ˋ���,��������ϐ�,�̏p,�̗͉񕜗�UP,�ϐk,�B�l�|,�e�ېߖ�,�e������,�n���w,
�����,����S,�ʏ�e�A�˖��,�D��ϐ�,�J�������l,�u�Ύg�p������,����ˌ�����,�ő�������,�őϐ�,
�݊�g��,�[���p,�j��,���j����ϐ�,���j��������,�����p�y�Z�z,�����p�y�́z,�����y��,��э���,�X�����U������,
�s��,�����ϐ�,����̈�v,������ϐ�,�ǖʈړ�,�ߊl���l,�A���̕�,�C�p,�C�e���U,�h��,��ბ�������,��ბϐ�,
������,�z��,�������U������,����̈�v,�������U������,�͂̉��,�Ӑg,��峎g��,�Αϐ�,�u���}��,���ϐ�,
�������S�l,�X�ϐ�,���ϐ�,���ϐ�,���C����

#Setting

```
pip install -r requirements.txt
```

# Use

```
python main.py --select "�U��,��_����,���؂�,����S"
```

# Output

```
Long-step dual simplex will be used
----------------------------------------------
['�U��', '��_����', '���؂�', '����S']
���ő�ɂ��鑕���͈ȉ��̂悤�ɂȂ�܂��B
������
Index(['�J�C�U�[�N���E��'], dtype='object', name='�h�')
Index(['�{���XS���C��'], dtype='object', name='�h�')
Index(['�q�s�m�A�[��'], dtype='object', name='�h�')
Index(['�h�[�x���R�C��'], dtype='object', name='�h�')
Index(['�C���S�b�gS�O���[��'], dtype='object', name='�h�')
-�h��X�L���ꗗ-
lv1     :lv[2]
lv2     :lv[3]
���؂�  :lv[5]
�U��    :lv[5]
��_����        :lv[2]
����S  :lv[1]
�h��    :lv[2]
�������U������  :lv[1]
���C����        :lv[1]

-�����i�X�L���ꗗ-
��_����        :lv1    �����iLv2
����S  :lv2    �����iLv2
----------------------------------------------
```