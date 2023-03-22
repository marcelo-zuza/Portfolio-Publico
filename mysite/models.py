from django.db import models
from django.db.models import signals
from stdimage import StdImageField
import uuid
from django.template.defaultfilters import slugify


def get_file_patch(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=200, null=False, blank=False)
    artista = models.CharField('Artista', max_length=200, default='')
    descricao = models.TextField('Descrição', max_length=300, null=False, blank=False)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, null=False, blank=False)
    foto = StdImageField(
        # As imagens serão importadas dentro da função que foi criada para gerar nomes aleatórios
        'Foto', upload_to=get_file_patch,
        # Aqui vai se definir a dimensao da imagens de entrada
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)


class LivroVisitas(Base):
    # ESCOLHAS = ('Sim', 'Sim'), ('Não', 'Não')
    nome = models.CharField('Nome', max_length=30, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=30, default='')
    comentario = models.TextField('Comentário', max_length=300, null=False, blank=False)
    # recomenda = models.CharField('Você recomenda o autor desta página?', max_length=6, choices=ESCOLHAS)

    def __str__(self):
        return self.nome


class Projetos(Base):
    nome = models.CharField('Nome', max_length=30, null=False, blank=False)
    descricao = models.TextField('Descrição', max_length=115)
    imagem = StdImageField('Imagem', upload_to=get_file_patch)
    link = models.CharField('Link', max_length=200, default='')

